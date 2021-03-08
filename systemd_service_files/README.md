# Add to /etc/systemd/system and enable with systemctl.
toonbox.service

# Replace or patch existing /lib/systemd/system/plymouth-quit.service unit file.
# This allows the Toonbox start time to be included in the plymouth progress
# bar and retains the Toonbox splash screen between video plays.
plymouth-quit.service

# Disable getty?
systemctl disable getty@.service
