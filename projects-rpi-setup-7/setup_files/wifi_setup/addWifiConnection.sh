sudo nmcli c add type wifi ifname wlan0 mode ap con-name pi_wifi ssid team_REPLACEWITHTEAMNUMBER_piREPLACEWITHPINUMBER
sudo nmcli c mod pi_wifi 802-11-wireless.band bg
sudo nmcli c mod pi_wifi 802-11-wireless.channel 1
sudo nmcli c mod pi_wifi 802-11-wireless-security.key-mgmt wpa-psk
sudo nmcli c mod pi_wifi 802-11-wireless-security.proto rsn
sudo nmcli c mod pi_wifi 802-11-wireless-security.group ccmp
sudo nmcli c mod pi_wifi 802-11-wireless-security.psk raspberry
sudo nmcli c mod pi_wifi ipv4.method shared
sudo nmcli c mod pi_wifi ipv4.addresses 192.168.REPLACEWITHTEAMNUMBER.REPLACEWITHPINUMBER/24
sudo nmcli c up pi_wifi

