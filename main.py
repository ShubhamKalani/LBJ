import csv
import time
class College:
	def __init__(self):
	    pass

	def set_college_data(self): #  For Registering College
	     time.sleep(0.5)
	     print("\nEnter Details of College\n")
	     try:
	        #Reading Input from user
	        self.college_id   = int(input("Enter College ID     : "))
	        self.college_name = input("Enter College Name   : ").title()
	        self.course  = input("Enter Course Type    : ").title()
	        self.city    = input("Enter City Name      : ").title()
	        self.fees    = int(input("Enter Fees           : "))
	        self.pincode = int(input("Enter PinCode        : "))
	        self.Details = [self.college_id , self.college_name , self.course , self.city, self.fees , self.pincode]

	        #Opening file in append mode
	        with open("College.csv", 'a') as csvfile: 
	            writer = csv.writer(csvfile)      # writer object 
	            writer.writerow(self.Details)     # writing details to csv file named with college.csv
	            time.sleep(0.5)
	            print("\nData Saved !\n")      
	     except:
	     	time.sleep(0.5)
	     	print("\n* * * * Invalid Data * * * *\n")

	def get_college_data(self): #For prining college data on the basis of city and course type

		#Reading Input from user 
		time.sleep(0.5)
		self.City   = input("Enter City     : ").title() 
		self.Course = input("Enter Course   : ").title()
		self.college_details = [] 
		
		#Opening file in read mode
		with open("College.csv" , 'r') as csvfile:
			reader = csv.reader(csvfile)
			# row[2] represent course type
			# row[3] represents city 
			# if both course and city matches with the user requirement append in to details
			for row in reader:
				if(row==[]) :
					continue 
				if(row[2] == self.Course and row[3] == self.City):
					self.college_details.append(row)
			# If no college found with the given requirements		
			if self.college_details == []:
				time.sleep(0.5)
				print("\n * * * * No College Found * * * * \n")
			else:  # Printing college details
				print("\n")
				time.sleep(0.5)
				print("College ID    College Name   Course  Type  City  Fees  PinCode\n\n")
				for line in self.college_details :
					print(*line,sep="        ")
					print()
	 
    # For deleting college from csv file on the basis of colleg ID 
	def delete_college_data(self):
		self.college_details = []
		#Reding input from user
		time.sleep(0.5)
		self.college_id = str(input("Enter College ID  : "))

		#Opening file in read mode
		with open("College.csv" , 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				if row == []:
					continue
				if row[0] != self.college_id:
					self.college_details.append(row)
				# ok = True  
				# for field in row :
				# 	if field ==  self.cllgID:
				# 		ok = False ;
				# 		break 

		#Opening File in write mode			
		with open("College.csv" , "w") as csvfile:
			writer = csv.writer(csvfile)

			#Updating File  
			for line in self.college_details:
				writer.writerow(line)

		time.sleep(0.5)
		print("\nFile Updated !\n")

			




 
	
		

print("\n  * * * * Welcome  * * * *\n\n")

Clg = College() #College Object

time.sleep(0.5)

print("Choose from below options\n")
print("1.Register College\n")
print("2.Display College\n")
print("3.Delete College\n")

while True :
	try:
		time.sleep(0.5)
		print()
		decision = input("Do you Wish to continue ? y / n : ").lower() 
		if decision == 'y':
			print()
			choice = int(input("Enter you choice: "))
			if choice == 1:
				Clg.set_college_data()
			elif choice == 2 :
				Clg.get_college_data() 
			elif choice == 3 :
				Clg.delete_college_data()
			else :
				time.sleep(0.5)
				print("\n * * * * Invalid Input * * * *\n")
		elif decision == 'n':
			    time.sleep(0.5)
			    print("\n  * * * * Good Bye * * * * \n")
			    break
		else :
			time.sleep(0.5)
			print("\n * * * * Invalid Input * * * * \n")
	except:
		time.sleep(0.5)
		print("\n * * * * Invalid Input * * * * \n")




