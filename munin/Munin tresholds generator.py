import socket
import sys

def ip_validate(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except AttributeError:
        try:
            socket.inet_aton(ip)
        except socket.error:
            return False
        return ip_str.count('.') == 3
    except socket.error:
        return False
    return True

def get_default_config(user_answer):
	sys.stdout = open("test.txt","w")
	print (f'[{hostname}]\n   {ip}\n   use_node_name yes\n')
	print ('   cpu.user.warning 200\n   cpu.user.critical 350\n   cpu.system.warning 200\n   cpu.system.critical 350\n')
	if type_hdd in 'HDD':
		print (f'   hddtemp_smartctl.{hdd_device_name}.warning 50\n   hddtemp_smartctl.{hdd_device_name}.critical 55\n')
	elif type_hdd in 'SSD':
		print (f'   hddtemp_smartctl.{ssd_device_name}.warning 68\n   hddtemp_smartctl.{ssd_device_name}.critical 70\n')
	if 'SSD HDD' in type_hdd or 'HDD SSD' in type_hdd:
		print (f'   hddtemp_smartctl.{hdd_device_name}.warning 50\n   hddtemp_smartctl.{hdd_device_name}.critical 55\n')
		print (f'   hddtemp_smartctl.{ssd_device_name}.warning 68\n   hddtemp_smartctl.{ssd_device_name}.critical 70\n')
	print ('   load.warning 2\n   load.critical 4\n')
	print ('   memory.swap.warning 1000000000\n   memory.swap.critical 3000000000\n   memory.active.warning 12000000000\n   memory.active.critical 15000000000\n   memory.free.warning 2400000000\n   memory.free.critical 800000000\n')
	if 'nginx' in other_soft_status:
		print ('   nginx_status.total.warning 1000\n   nginx_status.total.critical 10000\n   nginx_status.waiting.warning 1000\n   nginx_status.waiting.critical 10000\n')
	if 'postfix' in other_soft_status:
		print ('   postfix_mailqueue.hold.warning 100\n   postfix_mailqueue.hold.critical 200\n   postfix_mailqueue.incoming.warning 16000\n   postfix_mailqueue.incoming.critical 19000\n   postfix_mailqueue.active.warning 80000\n   postfix_mailqueue.active.critical 95000\n   postfix_mailqueue.deferred.warning 51200\n   postfix_mailqueue.deferred.critical 60800\n   postfix_mailqueue.corrupt.warning 100\n   postfix_mailqueue.corrupt.critical 200\n   postfix_mailqueue.maildrop.warning 64000\n   postfix_mailqueue.maildrop.critical 76000\n')
	print ('   processes.zombie.warning 50\n   processes.processes.warning 26214\n   processes.processes.critical 31129\n')
	if 'sendmail' in other_soft_status:
		print ('   sendmail_mailstats.rejected.warning 100\n   sendmail_mailstats.rejected.critical 200\n   sendmail_mailstats.discarded.warning 100\n   sendmail_mailstats.discarded.critical 200\n')
	print ('   sensors_temp.temp1.warning 81\n   sensors_temp.temp1.critical 90\n   sensors_temp.temp2.warning 81\n   sensors_temp.temp2.critical 90\n   sensors_temp.temp3.warning 81\n   sensors_temp.temp3.critical 90\n   sensors_temp.temp4.warning 81\n   sensors_temp.temp4.critical 90\n   sensors_temp.temp5.warning 81\n   sensors_temp.temp5.critical 90\n')
	if  'tomcat' in other_soft_status:
		print ('   tomcat_jvm.used.warning 80%\n   tomcat_jvm.used.critical 95%\n')
	print ('   uptime.warning 90\n   uptime.critical 365\n')
	sys.stdout.close()
	sys.stdout = open("/dev/stdout", "w")

while True:
	hostname = str(input('Set hostname: '))
	if not hostname:
		print ('Hostname is required!')
		continue
	else:
		break

while True:
	ip = str(input('Set ip address: '))
	result = ip_validate(ip)
	if not ip:
		print ('Ip address is required!')
	elif result is False:
		print ('Incorrect value! Please re-enter ip address!')
		continue
	else:
		break

while True:
	user_answer = str(input('Set configuration for munin server is default? (yes or no):\n'))
	if not user_answer:
		print ('Incorrect value! Please re-enter (yes or no)!\n')
	elif user_answer not in 'yes' and user_answer not in 'no':
		print ('Incorrect value! Please re-enter (yes or no)!\n')
		continue
	else:
		break

if user_answer in 'yes':
	while True:
		type_hdd = str(input('Select your type storage device? ("HDD" or "SSD" or "HDD SSD" or "SSD HDD"):\n'))
		if not type_hdd:
			print ('Incorrect value! Please re-enter ("HDD" or "SSD" or "HDD SSD" or "SSD HDD")!\n')
		elif type_hdd not in 'HDD' \
		and type_hdd not in 'SSD' \
		and type_hdd not in 'SSD HDD' \
		and type_hdd not in 'HDD SSD':
			print ('Incorrect value! Please re-enter ("HDD" or "SSD" or "HDD SSD" or "SSD HDD")!\n')
			continue
		else:
			break

	if 'SSD HDD' in type_hdd  or 'HDD SSD' in type_hdd:
		hdd_device_name = str(input('Set HDD device name:\n'))
		ssd_device_name = str(input('Set SSD device name:\n'))
	elif type_hdd in 'HDD':
		hdd_device_name = str(input('Set HDD device name:\n'))
	elif type_hdd in 'SSD':
		ssd_device_name = str(input('Set SSD device name:\n'))

	while True:
		other_soft_status = str(input('Does the host have additional software installed?\n(please specify separated by a space: nginx postfix sendmail tomcat) or "no"!\n'))
		if not other_soft_status:
			print ('Specify a value!')
		elif 'nginx' not in other_soft_status \
		and 'postfix' not in other_soft_status \
		and 'sendmail' not in other_soft_status \
		and 'tomcat' not in other_soft_status \
		and 'no' not in other_soft_status:
			print ('Incorrect value! Please re-enter!\n (please specify separated by a space: nginx postfix sendmail tomcat) or "no"!\n')
			continue
		else:
			break

	default_config = get_default_config(user_answer)
	print (f'The configuration is generated for the {hostname} host with ip address {ip}')

if user_answer in 'no':
	print ('Not implemented. Expect future releases.')