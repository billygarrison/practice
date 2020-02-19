import pysftp


# An *insecure* workaround to avoid needing to register AWS host keys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Connection info
host = "ec2-18-191-152-25.us-east-2.compute.amazonaws.com"
username = "ec2-user"
priv_key_file = "pysftp_test.pem"

# File locations
put_from = "test.txt"
put_to = "/home/ec2-user/test.txt"
get_from = put_to
get_to = "test2.txt"

# Create test file to put on server
with open(put_from, "w+") as f:
	f.write("Hello world!")

# Open SFTP connection to EC2 instance
with pysftp.Connection(host, username, private_key=priv_key_file, cnopts=cnopts) as sftp:
	# Put test file on server
	sftp.put(put_from, put_to)
	
	# Get test file from server
	sftp.get(get_from, get_to)