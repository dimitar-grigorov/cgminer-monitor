PI Mon
######

PI Mon is a zabbix script for monitoring cgminer hash rates

# Usage

 * Add the following line to your zabbix-agent.conf file on the host you are monitoring
 `UserParameter=cgminer.five_second_average,/usr/local/zabbix/plugins/pi_mon.py --host localhost --port 4028 `
 * Add an item on the zabbix server matching the item in UserParemeter `cgminer.five_second_average`
 * Restart Zabbix-Agent
