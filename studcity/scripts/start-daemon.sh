NAME=StudCity

systemctl daemon-reload
systemctl enable $NAME
systemctl start $NAME
systemctl status $NAME