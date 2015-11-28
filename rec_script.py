import string, sys, os

def main():
    main_letter_fname = sys.argv[1]
    address_list = sys.argv[2]

    f = open(address_list)
    for line in f.readlines():
        #error trap this line
        id,ret_address,location,salutation,posname = string.split(line,";")
        macro_file = "address_macro_%s" % id
        generate_macro(macro_file, [ret_address,salutation,location,posname])
#        texfile = main_letter_fname[:-4]+"_"+id+".tex"
        # insert macro into texfile
        # how to do? TBD
        # run latex
#        os.system()
        # delete unneeded files
    f.close()
    # end of loop over address_list

def generate_macro(macro_file, content_list):
    outf = open(macro_file,"w")
    command_list = ["\\newcommand{\\addressee}{%s}", "\\newcommand{\\dear}{%s}", "\\newcommand{\\yourplace}{%s}", "\\newcommand{\\jobname}{%s}"]

    for cmnd, cnt in zip(command_list,content_list):
         outstr = cmnd  % cnt
         outf.write(outstr+"\n")
    outf.close()
    return


main()
