NAME=Minusa

echo Starting deploy string for $NAME

cp /home/administrator/srsm_bot/minusa/$NAME.service /etc/systemd/system

./start-daemon.sh