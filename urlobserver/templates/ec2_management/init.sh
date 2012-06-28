#!/bin/bash
{% autoescape off %}

# create some public keys

# for root
mkdir -p /root/.ssh
chown root:root /root/.ssh
chmod 0700 /root/.ssh
{% for key in ssh_public_keys %}
echo '{{ key }}' >> /root/.ssh/authorized_keys
{% endfor %}
chmod 0600 /root/.ssh/authorized_keys

# for user named "ubuntu"
mkdir -p /home/ubuntu/.ssh
chown ubuntu:ubuntu /home/ubuntu/.ssh
chmod 0700 /home/ubuntu/.ssh
{% for key in ssh_public_keys %}
echo '{{ key }}' >> /home/ubuntu/.ssh/authorized_keys
{% endfor %}
chmod 0600 /home/ubuntu/.ssh/authorized_keys

# install tinyproxy
sudo apt-get --yes --force-yes update
sudo apt-get --yes --force-yes install tinyproxy

# Update tinyproxy config and reload the service
echo 'DisableViaHeader Yes' >> /etc/tinyproxy.conf
{% for ip in allowed_ips %}
echo 'Allow {{ ip }}' >> /etc/tinyproxy.conf
{% endfor %}
service tinyproxy restart

{% endautoescape %}
