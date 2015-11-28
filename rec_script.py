import string, sys, os, glob

def main():
    main_letter_fname = sys.argv[1]
    address_list = sys.argv[2]

    f = open(address_list)
    for line in f.readlines():
        # read info from address file
        try:
            id,full_addressee,ret_address,location,salutation,posname = string.split(line,";")
        except ValueError:
            print "Something wrong in %s, skipping" % line
            continue

        # insert macros into texfile
        texfile = main_letter_fname[:-4]+"_"+id+".tex"
        insert_macro(main_letter_fname,texfile, [full_addressee,ret_address,salutation,location,posname])

        # run latex
        os.system("pdflatex %s" % texfile)
    # end of loop over address_list
    f.close()

    # delete unneeded files
    texjunk = ["*.aux","*.log","*.synctex.gz"]
    for g in texjunk:
        for f in glob.glob(g):
            os.unlink(f)
    return


def generate_macro(outf, content_list):
    '''generates set of latex commands based on contents of content_list
       assumes specific format for content_list'''
    command_list = ["\\newcommand{\\addressee}{%s \\hfill\\today\\\\}", "\\newcommand{\\retaddress}{%s}", "\\newcommand{\\dear}{%s}", 
                    "\\newcommand{\\yourplace}{%s}", "\\newcommand{\\posname}{%s}"]

    for cmnd, cnt in zip(command_list,content_list):
         outstr = cmnd  % cnt
         outf.write(outstr+"\n")
    return

def insert_macro(orig_file, new_file, content_list):
    '''copies orig_file to new_file, inserting customized macro at position of address_macro'''
    inf = open(orig_file,"r")
    outf = open(new_file, "w")
    for line in inf.readlines():
        if "address_macro" in line:
            generate_macro(outf, content_list)
        else:
            outf.write(line)
    inf.close()
    outf.close()
    return


main()
