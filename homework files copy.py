#notesApp
# file_name = input("Please enter a filename: ")
# try:
#     file = open(file_name,"r" )
#     file.close()
#     print(" A) Read the file\n","B) Delete the file and start over\n","C) Append the file\n")
#     options = input("What would you like to do? : ")
#     if options == "a":
#         #read the file
#         file = open(file_name,"r")
#         print(file.read())
#     if options == "b":
#         #Delete the file and start over
#         file = open(file_name,"w")
#         insert_text = input("Please enter new text: ")
#         file.write(insert_text)
#     if options == "c":
#         #Append the file
#         file = open(file_name,"a")
#         add_more_text = input("Please enter more text: ")
#         file.write(add_more_text)
# except:
#     #Create new file and write to it.
#     file = open(file_name,"w")
#     text = input("Enter text here: ")
#     file.write(text)
# finally:
#     file.close()


# extra credit
import glob

for file_name in glob.glob("*.confirmit"):
    file = open(file_name,"r" )
    file.close()
    line = 0
    text = "HHNR	First name	Name	Zipcode	Place	District	County	County 2001	Region NUTS2	Size of Community 2006	Size of Community	Size of Community INT	Street	Email_Address	Telephone	ow_Home Internet	ow_Telephone	ow_Dish Washing Machine	ow_Refrigerator	ow_Deep Freezer	ow_Microwave Oven	ow_Washing Machine,self owned	ow_Wash_Machine with Dryer	ow_Clothes Dryer	ow_Vacuum cleaner robotic	ow_Bread Machine	ow_Soda Maker	ow_Electric tooth brush	ow_Electric Shaver	ow_Radio	ow_Colour TV	ow_Game Console	ow_PC	ow_Notebook	ow_Tablet	ow_Smartphone	ow_Coffee machine	ow_cof_Filter_coffee_machine	ow_cof_Pump_espresso	ow_cof_Bean_to_cup	ow_cof_Espresso machine	ow_cof_Combi_coffee_machine	ow_cof_POD_system	ow_Coffee machine - capsules	ow_cof_French_press	ow_cof_Moka_pot_electric	ow_cof_Moka_pot_NO_electric	ow_cof_Cezve	ow_cof_Philips	ow_cof_Eta	ow_cof_Ariete	ow_cof_POD_other	ow_cof_Dolce Gusto	ow_cof_Cafissimo	ow_cof_Tassimo	ow_cof_Nespresso	ow_cof_Cremesso	ow_cof_Illy	ow_cof_Mitaca	ow_cof_Lavazza	ow_cof_Zepter	ow_cof_Capsule machine other	ow_cof_most_used	ow_cof_acq_Filter_coffee	ow_cof_acq_Pump_espresso	ow_cof_acq_Bean_to_cup	ow_cof_acq_Espresso_machine	ow_cof_acq_Combi_coffee	ow_cof_acq_POD_system	ow_cof_acq_Capsule	ow_cof_acq_French_press	ow_cof_acq_Moka_pot_electric	ow_cof_acq_Moka_pot_NO_el	ow_cof_acq_Cezve	ow_cof_acq_Philips	ow_cof_acq_Eta	ow_cof_acq_Ariete	ow_cof_acq_POD_other	ow_cof_acq_Dolce_Gusto	ow_cof_acq_Cafissimo	ow_cof_acq_Tassimo	ow_cof_acq_Nespresso	ow_cof_acq_Cremesso	ow_cof_acq_Illy	ow_cof_acq_Mitaca	ow_cof_acq_Lavazza	ow_cof_acq_Zepter	ow_cof_acq_Capsule_other	ow_LK Albert	ow_LK Benu	ow_LK Billa	ow_LK CBA	ow_LK Coop	ow_LK DM	ow_LK Douglas	ow_LK Dr.Max	ow_LK FAnn	ow_LK Globus	ow_LK Iceland	ow_LK IKEA	ow_LK Kaufland	ow_LK Lidl	ow_LK Makro	ow_LK Marionnaud	ow_LK Marks&Spencer	ow_LK Penny market	ow_LK Pet	ow_LK Rossmanek	ow_LK Sephora	ow_LK Tchibo	ow_LK Tesco	ow_LK Teta	ow_LK Top_drogerie	ow_LK Yves Rocher	ow_LK Zabka	ow_LK Zverokruh	ow_LK Other	ow_Dog	ow_Cat	ow_Animals	ow_Bicycle	ow_E-scooter	ow_Motorcycle	ow_Car	ow_Car_Company	ow_No Traffic	HH Net Income	Char Completed"
    myFile = open(file_name, "r")
    list_of_lines = myFile.readlines()
    list_of_lines[line] = text + "\n"
    myFile = open(file_name, "w")
    myFile.writelines(list_of_lines)
    file.close()

