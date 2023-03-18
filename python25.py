gbl_name = "Matthew"
def alter_name():
    global gbl_name
    gbl_name = "Andrew Carnegie"

alter_name()
print(gbl_name)