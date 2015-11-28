import string, sys, os

def main():
    main_letter_fname = sys.argv[1]
    address_list = sys.argv[2]

    f = open(address_list)
    for line in f.readlines():
        #error trap this line
        id,full_addressee,ret_address,location,salutation,posname = string.split(line,";")
        # generate customized macro file for this address
        macro_file = "address_macro_%s" % id
        generate_macro(macro_file, [full_addressee,ret_address,salutation,location,posname])

        # insert macro into texfile
        texfile = main_letter_fname[:-4]+"_"+id+".tex"
        insert_macro(main_letter_fname,texfile, macro_file)

        # run latex
#        os.system("pdflatex %s" % texfile)
    # end of loop over address_list
    f.close()

    # delete unneeded files
    texjunk = ["*.aux","*.log","*.synctex.gz"]
    for g in texjunk:
        for f in glob.glob(g):
            os.unlink(f)
    return


def generate_macro(macro_file, content_list):
    outf = open(macro_file,"w")
    command_list = ["\\newcommand{\\addressee}{%s \\hfill\\today\\\\}", "\\newcommand{\\retaddress}{%s}", "\\newcommand{\\dear}{%s}", 
                    "\\newcommand{\\yourplace}{%s}", "\\newcommand{\\posname}{%s}"]

    for cmnd, cnt in zip(command_list,content_list):
         outstr = cmnd  % cnt
         outf.write(outstr+"\n")
    outf.close()
    return

def insert_macro(orig_file, new_file, macro_name):
    inf = open(orig_file,"r")
    outf = open(new_file, "w")
    for line in inf.readlines():
        if "address_macro" in line:
            line = "\\input{%s}" % macro_name
        outf.write(line)
    inf.close()
    outf.close()
    return


main()
