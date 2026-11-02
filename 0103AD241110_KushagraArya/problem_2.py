# input 1 : string : firstname : 'Rohit '
# input2 : string : lastname : 'Roy'
# input3 : integer : pincode : 426032(6digit)
# input 4 : N: 2(0<=N<=5)
#output : string : Usename
#fbname lname string length-small-first char-> lowercase 
#fname lname string length- large - Full string -> uppercase
#nth digit from beginning and end-> pincode 
#=> "rROHIT23"

# input 1 : string : firstname : 'kumar'
# input2 : string : lastname : 'kumud'
# input3 : integer : pincode : 426036(6digit)
# input 4 : N: 4 (0<=N<=5)
#output => "kKUMUD06"
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
pincode = input("Enter your pincode: ")
N = int(input("Enter a number between 0 and 5: "))
if len(fname) < len(lname):
    small = fname.lower()
    large = lname.upper()
else:
    small = fname.lower()
    large = lname.upper()

username = small[0] + large
username += pincode[N-1] + pincode[-N]
print("Your username is:", username)
