NAME=Minusa

echo Starting daemon string for $NAME

systemctl daemon-reload
systemctl enable $NAME
systemctl start $NAME
systemctl status $NAME