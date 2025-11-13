# CachyOS Wiki Offline
This document consolidates the English CachyOS wiki into a single offline-friendly Markdown file.

## Table of Contents
- [Overview](#overview)
  - [Welcome to the CachyOS Wiki](#index)
- [Cachyos Basic](#cachyos-basic)
  - [Changelogs](#cachyos-basic-changelogs)
    - [CLI Installer](#cachyos-basic-changelogs-cli-installer)
    - [GUI Installer](#cachyos-basic-changelogs-gui-installer)
  - [CachyOS FAQ & Troubleshooting Guide](#cachyos-basic-faq)
  - [Downloads and Validation](#cachyos-basic-download)
  - [How to navigate the CachyOS Wiki](#cachyos-basic-navigation-guide)
  - [Why CachyOS?](#cachyos-basic-why-cachyos)
- [Configuration](#configuration)
  - [Desktop Environments](#configuration-desktop-environments)
    - [Hyprland (Deprecated) Keybinds & FAQ](#configuration-desktop-environments-hyprland)
    - [i3wm Keybinds & FAQ](#configuration-desktop-environments-i3)
    - [Installing another DE/WM using CachyOS Settings](#configuration-desktop-environments-switch-desktop)
    - [KDE Plasma](#configuration-desktop-environments-kde)
    - [Niri Keybinds & FAQ](#configuration-desktop-environments-niri)
    - [Qtile Keybinds & FAQ](#configuration-desktop-environments-qtile)
  - [Automount Additional Drives Through fstab at Boot](#configuration-automount-with-fstab)
  - [Boot Manager Configuration](#configuration-boot-manager-configuration)
  - [Chromium-Based Browsers HW Acceleration](#configuration-enabling-hardware-acceleration-in-google-chrome)
  - [Dual GPU Setup Guide](#configuration-dual-gpu)
  - [Gaming with CachyOS Guide](#configuration-gaming)
  - [General System Tweaks](#configuration-general-system-tweaks)
  - [Post Install](#configuration-post-install-setup)
  - [sched-ext Tutorial](#configuration-sched-ext)
  - [Secure Boot Setup](#configuration-secure-boot-setup)
- [Features](#features)
  - [Chwd](#features-chwd)
    - [Managing Hardware with chwd](#features-chwd-chwd)
    - [Switching Between NVIDIA and AMD GPUs](#features-chwd-gpu-migration)
  - [CachyOS chroot Helper](#features-cachy-chroot)
  - [CachyOS Kernel](#features-kernel)
  - [CachyOS Settings](#features-cachyos-settings)
  - [Managing Linux Kernels & Sched-ext framework with the CachyOS Kernel Manager](#features-kernel-manager)
  - [Optimized Repositories](#features-optimized-repos)
- [Installation](#installation)
  - [Desktop Environments](#installation-desktop-environments)
  - [Filesystems](#installation-filesystem)
  - [Handheld Edition](#installation-installation-handheld)
  - [Offered Boot Managers](#installation-boot-managers)
  - [Preparation steps](#installation-installation-prepare)
  - [T2 MacBook](#installation-installation-t2macbook)
  - [CachyOS Installation Desktop/Laptop](#installation-installation-on-root)

<a id="overview"></a>
## Overview


<a id="index"></a>
### Welcome to the CachyOS Wiki

<a id="index-getting-started"></a>
### Getting Started

- [CachyOS FAQ & Troubleshooting Guide](#cachyos-basic-faq) — Find answers to common questions about CachyOS.
  
- [How CachyOS Improves Performance](#cachyos-basic-why-cachyos) — Check out the changes we make in order to improve performance.
  
- [Requirements & Preinstall setup](#installation-installation-prepare) — Making sure your system is ready for CachyOS installation.
  
- [Installation Guide](#installation-installation-on-root) — Step-by-step instructions to install CachyOS on your system.

<a id="cachyos-basic"></a>
## Cachyos Basic

<a id="cachyos-basic-faq"></a>
#### CachyOS FAQ & Troubleshooting Guide

> **Note:**
> The following questions & answers apply to CachyOS and Arch Based distributions. `This is not meant to replace the information on the Arch Linux Wiki`

> **Tip:**
> Stay alert to any official announcements from CachyOS on our [Forum](https://discuss.cachyos.org/c/announcements/8), Reddit post in our [official subreddit](https://www.reddit.com/r/cachyos/) or [Discord #annoucements](https://discord.com/channels/862292009423470592/873309651364610118) and [#updates-repo](https://discord.com/channels/862292009423470592/871739561364033566) regarding known issues with a package or updates that require manual intervention.

<a id="cachyos-basic-faq-how-to-report-an-issue-or-bug-to-cachyos"></a>
### How to report an issue or bug to CachyOS

> **Danger:**
> Be careful relying on help and commands provided by an AI model (like ChatGPT) without verifying the information from official sources. AI models can sometimes provide incorrect or misleading information, especially in technical contexts. Always cross-reference with trusted documentation or community resources.
>
> Otherwise you might end up with a completely broken system or make the issue even worse.

> **Tip:**
> Remember. In the Linux world there is an amazing quote: "Most likely someone else had the same issue before you." So please use the search function on Google, the Arch Wiki, or the CachyOS Forum/Discord before reporting an issue because it might already be solved.

> **Tip:**
> Don't forget to use the tldr command to view a simplified version of the man pages for commands you are not familiar with. Example:
>
> Some of the most common commands and descriptions for git:
> ```bash
> tldr git
> ```
>
> You can also combine tldr with a specific git command to get more detailed information about a parameter, for example:
> ```bash
> tldr git add
> ```

<a id="cachyos-basic-faq-places-to-report"></a>
#### Places to report

- [Github](https://github.com/CachyOS/distribution)
- [Forum](https://discuss.cachyos.org/c/feedback/bugreports/10)
- **Discord:** [Support Forum](https://discord.com/channels/862292009423470592/1400865136373403708)
- Before creating a new post. Please make sure to read the [Support Guidelines & Information](https://discord.com/channels/862292009423470592/1402210965700739082) pinned in the channel.
- Or if you think your issue can be solved quickly, use the [#support channel](https://discord.com/channels/862292009423470592/862294383470051348)
- [Reddit](https://www.reddit.com/r/cachyos/)

<a id="cachyos-basic-faq-be-patient-and-respectful"></a>
#### Be patient and respectful

The CachyOS team and community are volunteers who work on this in their free time. Please be patient and respectful when interacting with them. Providing a high-quality bug report is the best way to get your issue resolved quickly.

If you ask a vague question or provide insufficient information. Then you might get a vague response too or no response at all.

Here is an example:

- **Good question:**
- After a recent update (my last update was on DATE), my system fails to boot with a black screen. I have an NVIDIA GPU (model). I tried downgrading the `linux-cachyos` package to the previous version, but the issue persists. Here is the output of `journalctl -b -1` and `dmesg` from the live environment.
- **Bad or vague question:**
- My system is broken, please help me.
  
  **Otherwise you might end up looking like Abraham from this meme::**
   ![Image](src/assets/images/abraham-meme.jpg)
  

<a id="cachyos-basic-faq-describe-your-issue"></a>
#### Describe your Issue

Here is a couple of things you should ask yourself about:

- What is not working?
- Does downgrading package X fix the issue?
- Use the search function for equal issues
- Did the issue appear after an update?
- Have you made modifications on your own?
- Example: `Adding an additional flag in a modprobe file`
- Is it hardware related? (e.g. GPU, WiFi, etc.)
- Is it software related? (e.g. specific application, desktop environment, etc.)
- Is it a fresh installation or did the issue appear after some time of usage?

<a id="cachyos-basic-faq-how-to-gather-logs"></a>
### How to gather logs

There are many ways to gather logs from your system. Here are a couple of examples and tools you can use:

<a id="cachyos-basic-faq-creating-a-general-bug-report"></a>
#### Creating a general bug report
- CachyOS provides a great tool to gather logs from the system called `cachyos-bugreport.sh`.
- This tool will collect logs from:
- `dmesg`
- `journalctl`
- `inxi` (To collect hardware information)
- When the logs are collected, the user will be prompted to decide whether to upload them to our paste website.
- Run the following command in the terminal, and post the link with the bugs into the topic:
    ```sh
    sudo cachyos-bugreport.sh
    ```

<a id="cachyos-basic-faq-gathering-logs-from-a-program-that-is-not-starting"></a>
#### Gathering logs from a program that is not starting
- X program is no longer starting:
- There are many reasons why a graphical program might not start. The best way to gather logs for this kind of issue is to run the program from a terminal. This way you can see any error messages or output that might help diagnose the problem.
- Example:
    ```sh
    firefox
    ```
- If Firefox fails to start, you might see an error message in the terminal that can help identify the issue.
> **Tip:**
> If you want to save the output to a text file for easier sharing, you can redirect the output like this:
> ```sh
> firefox &> firefox-log.txt
> ```
> Remember to press `CTRL + C` to terminate the process after it fails to start so the terminal writes the output to the file.

<a id="cachyos-basic-faq-check-the-latest-updated-packages-in-pacman"></a>
#### Check the latest updated packages in pacman.

To get a list of the most recently updated packages on your system, you can use the following command:

```bash
grep "\[ALPM\] upgraded" /var/log/pacman.log | tail -n 50
```

> **Tip:**
> Adjust the `-n` parameter of tail to get more of less lines.

<a id="cachyos-basic-faq-keybinds-for-navigating-in-journalctl-and-dmesg"></a>
#### Keybinds for navigating in journalctl and dmesg

Most common Keybinds to navigate through the logs when less is or human readable mode is being used:

`Arrow Keys`: to move up and down line by line.

`Page Down & Page Up or Ctrl + A/D` : to scroll down or up one page at a time.

`j & k`: to move down or up line by line (similar to Vim).

`g or Home`: to jump to the beginning of the log.

`Shift + G or End`: to jump to the end of the log.

<a id="cachyos-basic-faq-using-journalctl-to-gather-system-logs"></a>
#### Using journalctl to gather system logs

The `journalctl` command is an extremely useful tool for viewing system logs. Here are some of the most common and useful command combinations.

<a id="cachyos-basic-faq-basic-usage-and-common-examples"></a>
##### Basic usage and common examples

> **Tip:**
> Combine multiple options for more specific filtering.

**View the entire log (from oldest to newest)::**
```bash
journalctl
```

**View logs from the current boot only::**
```bash
journalctl -b
```

**Security and authentication problems::**
```bash
journalctl -u sshd -u polkit -b -0 | grep -i "fail\|error\|denied"
```
Look for authentication failures and security policy denials.

**Following logs in Real Time::**
```bash
journalctl -f
```
> **Tip:**
> Combine this with other filters. For example:
> ```bash
> # Following logs from Adguard Home service:
> journalctl -u adguardhome -f
> ```

**Audio issues from the current boot:**
```bash
journalctl --user -u pipewire -u pipewire-pulse -u wireplumber -b 0
```
View logs from audio services to troubleshoot sound issues.

**Memory (RAM) errors::**
```bash
journalctl -k | grep -i "memory\|ram"
```
Look for memory corruption or detection issues.

**Bluetooth related issues::**
```bash
# From the current boot:
journalctl -u bluetooth -b 0
journalctl -u bluetooth -b 0
# From the previous boot:
journalctl -u bluetooth -b -1
```

<a id="cachyos-basic-faq-time-based-filtering"></a>
###### Time based Filtering

**View logs from the last few minutes/hours::**
```bash
journalctl --since "10 minutes ago"
journalctl --since "1 hour ago"
journalctl --since "2024-01-15 14:30:00"
```

**View logs from a specific time range::**
```bash
journalctl --since "09:00" --until "10:00"
```

<a id="cachyos-basic-faq-filtering-by-priority-and-service-or-program"></a>
###### Filtering by Priority and Service or Program

Possible priority levels are: `debug`, `info`, `notice`, `warning`, `err`, `crit`, `alert`, `emerg`.

Or by using numbers:

`0` equals `emerg`

`1` equals `alert`

`2` equals `crit`

`3` equals `err`

`4` equals `warning`

`5` equals `notice`

`6` equals `info`

and `7` equals `debug`.

**Show only error, critical and emergency messages::**
```bash
journalctl -p err..emerg
```
> **Tip:**
> You can combine these with the previous examples:
>
> Example:
> ```bash
> journalctl -p err..emerg --since "9:00" --until "10:00"
> ```

**Show logs from a specific system service::**
```bash title='Examples'
# View logs from the NetworkManager service:
journalctl -u NetworkManager
# View logs from the GDM (GNOME Display Manager) service:
journalctl -u gdm
# View logs from the SDDM (Simple Desktop Display Manager) service:
journalctl -u sddm
```

**Show logs from a specific Process ID (PID)::**
```bash
journalctl _PID=pid
# Example:
journalctl _PID=3344
```

**Show logs from a specific executable::**
```bash
journalctl path/to/executable
# Example:
journalctl /usr/bin/firefox
```

<a id="cachyos-basic-faq-using-journalctl-to-check-kernel-messages"></a>
#### Using journalctl to check kernel messages

> **Note:**
> When to use `journalctl -k`  vs `dmesg`:
>
> - `journalctl -k` accesses kernel messages stored in the systemd journal (persistent across reboots if configured and offers better integration with time based filtering and journal features.
> - `dmesg` reads the current kernel ring buffer (volatile, lost after reboot)

**Basic kernel message viewing::**
```bash
journalctl -k
```
Shows all kernel messages from the journal, equivalent to `dmesg` but from the journal's perspective.

**Current boot kernel messages only::**
```bash
journalctl -k -b 0
```
Displays kernel messages from the current boot session only.

**Previous boot kernel messages::**
```bash
journalctl -k -b -1
```
View kernel messages from the previous boot. Useful for diagnosing boot failures or crashes.

**Follow new kernel messages in real time::**
```bash
journalctl -k -f
```
Watch kernel messages as they occur, great for monitoring hardware events or driver loading.

**Search for specific driver messages::**
```bash
# Examples:
# GPU related messages:
journalctl -k | grep -i "nvidia\|amd\|intel"
# USB device messages:
journalctl -k | grep -i "usb\|pci"
```

**Time based kernel message filtering::**
```bash
journalctl -k --since "1 hour ago"
journalctl -k --since "09:00" --until "10:00"
```
View kernel messages from specific time periods.

<a id="cachyos-basic-faq-using-dmesg-for-kernel-messages"></a>
#### Using dmesg for Kernel Messages

The `dmesg` command displays the kernel ring buffer, which contains messages from the kernel about hardware detection, driver initialization and system events.

<a id="cachyos-basic-faq-basic-usage-and-formatting"></a>
##### Basic Usage and Formatting

**View the entire kernel message buffer::**
```bash
dmesg
```

**View with human-readable timestamps::**
```bash
dmesg -T
```

**View in a pager for easier reading::**
```bash
dmesg | less
```

<a id="cachyos-basic-faq-filtering-by-priority-level"></a>
##### Filtering by Priority Level

Similar to journalctl, dmesg allows filtering messages by priority level.

**Show only errors and critical messages::**
```bash
dmesg -l err,crit,alert,emerg
```
Possible priority levels are: `debug`, `info`, `notice`, `warning`, `err`, `crit`, `alert`, `emerg`.

Or by using numbers:

`0` equals `emerg`

`1` equals `alert`

`2` equals `crit`

`3` equals `err`

`4` equals `warning`

`5` equals `notice`

`6` equals `info`

and `7` equals `debug`.

**View the most recent kernel messages::**
```bash
dmesg -w
```

**Search for specific hardware or driver messages::**
```bash
# Examples:
# To search for USB related messages:
dmesg | grep -i usb | less
# Bluetooth devices:
dmesg | grep -i bluetooth
# NVIDIA related:
dmesg | grep -i nvidia | less
# Devices failing to initialize:
dmesg | grep -i "error\|failed" | less
```

<a id="cachyos-basic-faq-common-examples-for-specific-issues-using-dmesg"></a>
###### Common examples for specific issues using dmesg

**When a USB device isn't recognized::**
```bash
dmesg -w | grep -i usb
```
Then plug in the device and watch for new messages.

**GPU initialization issues::**
```bash
dmesg | grep -i "nvidia\|amd\|intel\|radeon\|drm\|gpu" | less
```

**WiFi or network adapter issues::**
```bash
dmesg | grep -i "wlan\|wifi\|network\|firmware" | tail -20
```
Check for missing firmware loads or driver errors that prevent your wireless card from working.

**HDD/SSD detection problems::**
```bash
dmesg | grep -i "sda\|sdb\|nvme\|scsi\|disk" | head -30
```
Use this when a storage device isn't being detected or shows errors during boot.

**System freezes or kernel panics::**
```bash
dmesg -T -l emerg,alert,crit,err | tail -30
```
Check the most severe kernel messages that occurred before a system crash or freeze.

**Memory (RAM) errors::**
```bash
dmesg | grep -i "memory\|ram"
```
Look for memory corruption, detection issues, or ECC error reports.

**Audio device events::**
```bash
dmesg | grep -i "audio\|snd\|hda" | grep -i "error\|fail\|card"
```
Check if your sound card is being detected properly and if drivers are loading correctly.

**Kernel module loading failures::**
```bash
dmesg | grep -i "module\|init" | grep -i "error\|fail"
```
When specific hardware drivers aren't loading or are failing to initialize.

**Real-time monitoring for hardware events::**
```bash
dmesg -w -l warn,err,crit,alert,emerg -T
```
Continuously watch for new important kernel messages while you reproduce an issue.

**BIOS/UEFI and firmware issues::**
```bash
dmesg | grep -i "bios\|uefi\|firmware\|efi"
```
Check for compatibility issues between your hardware firmware and the Linux kernel.

<a id="cachyos-basic-faq-installation-live-environment"></a>
### Installation & Live Environment

<a id="cachyos-basic-faq-why-does-the-cachyos-live-iso-only-include-kde-plasma"></a>
#### Why does the CachyOS live ISO only include KDE Plasma?

We've chosen to focus our development and maintenance efforts exclusively on the KDE Plasma desktop environment. This allows us to deliver a more polished, stable, and consistent user experience on our live ISO.

The live environment is primarily intended for installing CachyOS or using cachy-chroot for system recovery. For a safe way to test other desktop environments or window managers, we highly recommend trying them in a virtual machine (VM).

<a id="cachyos-basic-faq-why-does-the-installer-take-so-long-to-start-after-clicking-launch-installer"></a>
#### Why does the installer take so long to start after clicking "Launch Installer"?

> **Caution:**
> Make sure you have an active/running internet connection, otherwise nothing will happen after you press this button.

The installer is not frozen. It is running a necessary background script to prepare your system for installation. This process ensures your system's keyrings and clock are up-to-date, which helps prevent common installation issues.

[View the script on GitHub](https://github.com/CachyOS/CachyOS-Live-ISO/blob/master/archiso/airootfs/usr/local/bin/calamares-online.sh) to have a better understanding of what it does.

  1. Removes old keyring files.
  2. Installs and updates the latest Arch Linux & CachyOS keyring packages.
  3. Initializes and populates the pacman keyring.
  4. Enables network time synchronization.
  5. Checks your system's boot type (UEFI or BIOS/MBR) to prompt the user to select a bootloader depending on the type.

This is why it can take a bit of time to load the installer.

<a id="cachyos-basic-faq-why-does-my-installation-get-stuck-at-33"></a>
#### Why does my installation get stuck at 33%

This happens when the installer is struggling to download packages. It's usually a sign of a very slow or unstable internet connection. Please check your network connection and try again.

<a id="cachyos-basic-faq-bootloader-recovery-and-btrfs-snapshots"></a>
### Bootloader Recovery and Btrfs snapshots

> **Note – In case of a deleted /boot partition. Please create a new one following the respective [partition scheme:**

<a id="cachyos-basic-faq-steps-to-recover-your-bootloader"></a>
#### Steps to recover your bootloader

> **Tip:**
> If you're unsure on how to use `cachy-chroot`, please refer to the [CachyOS chroot Helper](#features-cachy-chroot) documentation first.

1. Boot into the CachyOS Live ISO.
2. Open a terminal and chroot into your installed system using the `cachy-chroot` command.

        ```bash
        sudo cachy-chroot
        ```
    If your system is utilizing BTRFS with our preset say `y` in the prompt:
         ```bash title='Example'
         Do you want to use CachyOS BTRFS preset to auto mount root subvolume? y
         Do you want to mount additional partitions? · yes
         Enter the mount point for additional partition (e.g. /boot) type 'skip' to cancel:
         # Type /boot for systemd-boot, Limine or rEFInd
         # Type /boot/efi for GRUB
         ```
3. Follow the instructions below for your installed bootloader and system type (UEFI or MBR/BIOS).
    
        
<a id="cachyos-basic-faq-grub"></a>
###### GRUB

            Reinstall GRUB with the following command:
            
                
<a id="cachyos-basic-faq-uefi"></a>
###### UEFI

                        ```bash
                        sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=cachyos
                        ```
                

                
<a id="cachyos-basic-faq-mbrbios"></a>
###### MBR/BIOS

                        ```bash
                        sudo grub-install --target=i386-pc /dev/sdX # Replace sdX with your disk e.g. sda
                        ```
                

            
        

        
<a id="cachyos-basic-faq-systemd-boot-uefi-only"></a>
###### systemd-boot (UEFI only)

            Reinstall systemd-boot with the following command:
                ```bash
                sudo bootctl install
                ```
        

        
<a id="cachyos-basic-faq-limine"></a>
###### Limine

            Reinstall Limine with the following command:
            
                
<a id="cachyos-basic-faq-uefi"></a>
###### UEFI

                        ```bash
                        sudo limine-install
                        ```
                

                
<a id="cachyos-basic-faq-mbrbios"></a>
###### MBR/BIOS

                        ```bash
                        sudo limine bios-install /dev/sdX # Replace sdX with your disk e.g. sda
                        ```
                

            
        

        
<a id="cachyos-basic-faq-refind-uefi-only"></a>
###### rEFInd (UEFI only)

            Reinstall rEFInd with the following command:
                ```bash
                sudo refind-install
                ```
        

    
4. Reinstall the CachyOS kernel:
        ```bash
        sudo pacman -Syu linux-cachyos linux-cachyos-headers
        ```
5. Exit from cachy-chroot:
        ```bash
        exit
        ```
6. Reboot your system.

<a id="cachyos-basic-faq-using-a-btrfs-snapshot-as-a-rollback-point"></a>
#### Using a Btrfs snapshot as a rollback point

> **Note:**
> Even though CachyOS automatically creates Btrfs snapshots before each system update with the usage of pacman hooks, it's always a good idea to create your own snapshots before making major changes to your system.

A BTRFS snapshot appears as an additional boot entry in your bootloader menu and is usually named something like:
- `10 | 10-30-2025 14:37:10`

**Example in a screenshot::**
![Image](src/assets/images/btrfs-snapshot-boot-entry.jpg)

You can also use the Btrfs Assistant application to manage your snapshots. It provides a graphical interface to create, delete, and restore snapshots.

**Screenshot of Btrfs Assistant::**
![Image](src/assets/images/btrfs-assistant-example.png)

<a id="cachyos-basic-faq-package-management-updates"></a>
### Package Management & Updates

<a id="cachyos-basic-faq-pacman-troubleshooting"></a>
#### Pacman Troubleshooting

<a id="cachyos-basic-faq-error-signature-is-invalid"></a>
##### error: signature is invalid

This error indicates a problem with the cryptographic signature of a package. It is usually caused by an outdated mirror or a broken keyring on your system.

While mirrors often fix themselves after a short while, if the issue persists, you should try one of the following two solutions.

<a id="cachyos-basic-faq-first-solution-resync-pacman-mirrors"></a>
###### First Solution: Resync Pacman Mirrors

```sh
sudo pacman -Syu
```

<a id="cachyos-basic-faq-second-solution-rate-your-mirrors"></a>
###### Second Solution: Rate Your Mirrors

```sh title='Rate your mirrors'
sudo cachyos-rate-mirrors
```

<a id="cachyos-basic-faq-third-solution-reset-keyrings"></a>
###### Third Solution: Reset Keyrings

If rating your mirrors doesn't work, it's likely your system's keyrings are broken.

- Open CachyOS Hello and navigate to **Apps/Tweaks**.
- Click the Reset keyrings button.

<a id="cachyos-basic-faq-error-404-not-found"></a>
##### error: 404 Not Found

This error means the package you are trying to install is not available on your current mirror. This usually happens when your local package database is out of sync with the remote repositories.

**Solution:**

Run the following command to refresh your package database and perform a full system upgrade. This will ensure your system knows about the latest available packages.

```sh
sudo pacman -Syu
# Then try to install the package you want again.
```

<a id="cachyos-basic-faq-error-could-not-remove"></a>
##### error: could not remove

This error occurs when the pacman cache contains files that the system cannot automatically manage. This is a common issue that can be easily fixed.

- Solution 1: Use CachyOS Hello.
- The simplest way to fix this is with CachyOS Hello. Open it and go to **Apps/Tweaks**, then click the **Clear package cache** button.

- Solution 2: Manually remove the cache.
- Run the following command to remove all orphaned packages from the cache.
  ```sh
  sudo rm -r /var/cache/pacman/pkg/*
  ```

<a id="cachyos-basic-faq-error-file-is-corrupted-invalid-or-corrupted-package-pgp-signature"></a>
##### error: File is corrupted (invalid or corrupted package (PGP signature))

```sh
# Example:
:: File /var/cache/pacman/pkg/python-charset-normalizer-3.4.0-1-any.pkg.tar.zst
is corrupted (invalid or corrupted package (PGP signature)).
```

This error typically indicates a problem with your system's pacman keyrings, which verify the authenticity of packages. The following commands will reset and re-populate the keyrings to resolve the issue.

```sh
sudo rm -rf /etc/pacman.d/gnupg/
sudo pacman-key --init
sudo pacman-key --populate

sudo pacman-key --recv-keys F3B607488DB35A47 --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key F3B607488DB35A47

sudo rm -R /var/lib/pacman/sync
```

<a id="cachyos-basic-faq-error-unable-to-lock-database"></a>
##### error: unable to lock database

This error occurs when another pacman process is already running, which locks the database to prevent corruption. If the previous process crashed or was interrupted, the lock file `db.lck` might not have been removed.

- Solution 1: Use CachyOS Hello
- The simplest way to fix this is with the **Remove db lock** function in the **Apps/Tweaks** tab of CachyOS Hello

- Solution 2: Remove the lock file manually
- If you prefer not to use CachyOS Hello, you can remove the lock file manually:

```sh
sudo rm /var/lib/pacman/db.lck
```

<a id="cachyos-basic-faq-error-failed-retrieving-file-connection-timed-out"></a>
##### error: failed retrieving file ... Connection timed out

You might see errors like these:

```text
# Example errors:
error: failed retrieving file '...' from ... : Connection timed out
error: failed retrieving file '...' from ... : Couldn't resolve host name
error: failed retrieving file '...' from ... : The requested URL returned error: 526
```

These errors almost always indicate a problem with your current mirrors. They may be slow, temporarily down, or unreachable from your location.

- Solution: The best way to fix this is to update your mirror list with faster and more reliable mirrors.

```sh
sudo cachyos-rate-mirrors
# Afterwards, you can update your system with:
sudo pacman -Syu
```

> **Tip:**
> The `cachyos-rate-mirrors` command tests available CachyOS mirrors based on speed and synchronization status, then updates your mirror list file (`/etc/pacman.d/cachyos-mirrorlist`) with the best-performing ones.
>
> Consider running it periodically, especially if you notice slowdowns during system updates.

<a id="cachyos-basic-faq-warning-local-is-newer-than"></a>
##### warning: local is newer than...

This warning appears when a package version on your system is newer than the version available in the official repositories. This can happen if a mirror is out of date or if a package was downgraded in the repositories or if a package was installed from a different source.

- Solution: the `pacman -Syuu` command performs a full system upgrade and allows for downgrades, which will fix the warning by synchronizing your local packages with the repository versions.

```sh title='To remove these warnings, execute the following command:'
sudo pacman -Syuu
```

<a id="cachyos-basic-faq-error-failed-to-commit-transaction-conflicting-files"></a>
##### error: failed to commit transaction (conflicting files)

This error indicates that pacman is trying to install or update a package that contains files already present on your system from a different source. This is a built-in safety feature to prevent system breakage.

- Solution: You can resolve this issue by removing the conflicting files manually. For more information and solutions, please refer to the [Arch Wiki](https://wiki.archlinux.org/title/Pacman#%22Failed_to_commit_transaction_(conflicting_files)%22_error).

```sh title='Example'
error: failed to commit transaction (conflicting files)
nvidia-utils: /usr/lib/environment.d/10-gsk.conf exists in filesystem
Errors occurred, no packages were upgraded.
 -> error installing repo packages
```

To fix this specific example, you would remove the conflicting file and then run your update command again.

```sh
sudo rm /usr/lib/environment.d/10-gsk.conf
```

<a id="cachyos-basic-faq-error-module-not-found-nvidia-nvidiamodeset"></a>
##### ERROR: module not found: 'nvidia', 'nvidia_modeset', ...

```sh title='Example'
==> ERROR: module not found: 'nvidia'
==> ERROR: module not found: 'nvidia_modeset'
==> ERROR: module not found: 'nvidia_uvm'
==> ERROR: module not found: 'nvidia_drm'
```

**Two reasons for this error:**

1) Since Early Module Loading is always enabled in chwd, mkinitcpio consistently expects the presence of NVIDIA modules; this error arises when those modules are missing.

2) You might be missing NVIDIA modules from other installed kernels on your system.

```sh title='Install the following package to fix this error'
sudo pacman -S nvidia
```

<a id="cachyos-basic-faq-specific-software-issues"></a>
#### Specific Software Issues

<a id="cachyos-basic-faq-discord-asks-for-an-update-that-isnt-available-in-the-repositories"></a>
##### Discord asks for an update that isn't available in the repositories.

![Image](src/assets/images/discord-update.png)

This happens because Discord uses its own update system, which gets ahead of the official repositories. A new version of the app has been released, but it hasn't been packaged for our mirrors yet.

In order to get around this issue, follow [Arch Wiki's fix guide](<https://wiki.archlinux.org/title/Discord#Discord_asks_for_an_update_not_yet_available_in_the_repository>).

<a id="cachyos-basic-faq-general-questions"></a>
#### General questions

<a id="cachyos-basic-faq-what-is-the-interval-on-which-git-packages-are-updated"></a>
##### What is the interval on which -git packages are updated?

Usually once on Monday, though there may be exceptions.

<a id="cachyos-basic-faq-do-the-bin-packages-in-the-cachyos-repositories-benefit-from-the-same-performance-optimizations"></a>
##### Do the -bin packages in the CachyOS repositories benefit from the same performance optimizations?

No. The `-bin` packages are precompiled binaries and do not include the same performance optimizations as the source based packages in the CachyOS repositories.

<a id="cachyos-basic-faq-how-to-disable-the-boot-loading-animation-plymouth"></a>
##### How to disable the boot loading animation (Plymouth)

> **Note – This could solve a black screen issue on some systems e.G. with old NVIDIA GPUs:**

To disable the boot loading animation, you need to edit your [bootloader configuration](#configuration-boot-manager-configuration) and add the following kernel parameters:

```sh
plymouth.enable=0 disablehooks=plymouth
```

> **Note – systemd-boot, GRUB and Limine require regenerating the initramfs images:**
> systemd-boot: `sudo sdboot-manage gen`
>
> GRUB: `sudo grub-mkconfig -o /boot/grub/grub.cfg`
>
> Limine: `sudo limine-mkinitcpio`

<a id="cachyos-basic-faq-submitting-package-requests-to-cachyos"></a>
##### Submitting Package Requests to CachyOS

CachyOS offers an extensive list of precompiled AUR Packages, which are commonly used.
Users can create requests for AUR packages, which, if approved, are automatically updated by our build server

If you want us to add a package, you can submit a request on GitHub or in the forum.

- [GitHub:](https://github.com/CachyOS/distribution/issues)
- [Forum:](https://discuss.cachyos.org/c/feedback/repository/11)
- [Discord: Feedback Channel](https://discord.com/channels/862292009423470592/1150723027986813018)

<a id="cachyos-basic-faq-security-best-practices"></a>
### Security & Best Practices

<a id="cachyos-basic-faq-aur-safety-practices"></a>
#### AUR Safety Practices

The AUR offers a vast selection, but security is paramount. Here’s a concise guide to safe AUR usage for your CachyOS system.

* **1. Understand the PKGBUILD:** It's the build script. Know its structure, variables (`source`, `pkgname`), and functions (`build()`, `package()`).
* **2. Verify Source Links:** Always check that `source` URLs point to official project sites or trusted repositories. Avoid suspicious or personal links.
* **3. Review Installation Steps:** Inspect where files are installed (`package()` function) and if any commands are unusual or touch sensitive system areas. Check `.install` scripts too.
* **4. Research the Maintainer:** Look into the maintainer's history on the AUR for any past security issues or suspicious activity.
* **5. Check Checksums & PGP:** Absolutely crucial! Confirm all checksums (SHA256, BLAKE2b, etc.) match upstream. Use PGP signatures (`validpgpkeys`) for authenticity when available.
* **6. Be Cautious with `-bin` Packages:** These use pre-compiled binaries, meaning you can't inspect the source. Apply maximum scrutiny to their origins and integrity.
* **7. Read Community Comments:** Check the AUR page comments for warnings, issues, or insights from other users.
* **8. Never Skip Integrity Checks:** Using `--skipinteg` or similar flags bypasses all security checks. Don't do it.
* **9. Control Your AUR Helper:** Understand how your helper (yay, paru) works. Ensure it shows you the PKGBUILD and its diffs, or build manually with `makepkg`.
* **10. Assess Necessity:** Before installing, ask if you truly need this AUR package, or if an official repo alternative exists.
* **11. Keep Your System Updated:** Regularly run `sudo pacman -Syu` to ensure all your system components, including `pacman` and `makepkg`, have the latest security patches.

Stay vigilant to keep your Arch-based system secure!

<a id="cachyos-basic-faq-choosing-a-gui-package-manager"></a>
#### Choosing a GUI Package Manager

While graphical package managers offer convenience, certain ones are known to cause severe issues on rolling-release systems like CachyOS and should be avoided for managing system packages.

-   **Pamac:** is known to improperly handle certain package management tasks, such as corrupting system package keyrings. This can lead to PGP signature errors that prevent you from updating your system.

-   **Discover (KDE) & GNOME Software Center:** These app stores use the PackageKit backend. While they're generally safe for managing Flatpaks, using them to install or update **system packages** is risky. PackageKit-based managers can also be unstable or prone to crashing, which could leave your system in a broken state after a failed transaction.

For maximum stability and reliability, we **highly recommend** managing system packages through the command line with `pacman`

If you prefer a graphical interface, GUI front-ends like **[Octopi](</configuration/post_install_setup/#updating-the-system>)** or the **CachyOS Package Installer** are considered as safe alternatives, as they are more direct wrappers for pacman functionality.

<a id="cachyos-basic-download"></a>
#### Downloads and Validation

<a id="cachyos-basic-download-official-iso-sources"></a>
### Official ISO Sources

CachyOS ISO can be obtained from the following sources:

*   [Website](<https://cachyos.org/download>)
*   [SourceForge](<https://sourceforge.net/projects/cachyos-arch/files/>)
*   [CachyOS Mirror](<https://mirror.cachyos.org/ISO/>)

<a id="cachyos-basic-download-verifying-iso-integrity-with-sha256"></a>
### Verifying ISO integrity with SHA256

> **Caution – WARNING:**
> Always take an extra step to verify the ISO's integrity to avoid any undesired issues at installation or while creating a bootable media.

**Current ISO Version:** `250828`

**SHA256 Hash:** `83ab50783ed41bff0f497b223a78312edef7d4d718f22baf7a6b01a6eb85d88b`

<a id="cachyos-basic-download-windows"></a>
###### Windows

1. Download the [file](https://mirror.cachyos.org/ISO/desktop/250828/cachyos-desktop-linux-250828.iso.sha256) containing the SHA256 hash **(Open it with a Text Editor e.g. Notepad).**
2. Open CMD or PowerShell as Administrator and [navigate](<https://www.wikihow.com/Change-Directories-in-Command-Prompt>) to the path where the ISO and SHA256 files are stored.
3. Execute the following command:
   ```powershell
   # Example:
   certUtil -hashfile cachyos-desktop-linux-250828.iso SHA256
   ```
4. Compare the certUtil hash output to the one from the downloaded file in **Step 1**. If they match, you can proceed with the CachyOS installation.

<a id="cachyos-basic-download-linux"></a>
###### Linux

1. Download the [file](https://mirror.cachyos.org/ISO/desktop/250828/cachyos-desktop-linux-250828.iso.sha256) containing the SHA256 hash.
2. Open a terminal, navigate to the directory containing the `.sha256` file, and execute the following commands:
   ```sh
   # Example:
   cd Downloads/
   cat cachyos-desktop-linux-250828.iso.sha256
   # 83ab50783ed41bff0f497b223a78312edef7d4d718f22baf7a6b01a6eb85d88b
   ```
3. Compare the output from **Step 2** and execute the following command to check the ISO file's hash:
   ```sh
   # Example:
   sha256sum cachyos-desktop-linux-250828.iso
   ```
4. If the hashes from **Step 2** and **Step 3** match, you can proceed with the CachyOS installation.

<a id="cachyos-basic-download-macos"></a>
###### macOS

1. Download the [file](https://mirror.cachyos.org/ISO/desktop/250828/cachyos-desktop-linux-250828.iso.sha256) containing the SHA256 hash.
2. Open a terminal, navigate to the directory containing the `.sha256` file, and execute the following commands:
   ```sh
   # Example:
   cd Downloads/
   cat cachyos-desktop-linux-250828.iso.sha256
   # 83ab50783ed41bff0f497b223a78312edef7d4d718f22baf7a6b01a6eb85d88b
   ```
3. Compare the output from **Step 2** and execute the following command to check the ISO file's hash:
   ```sh
   # Example:
   shasum -a 256 cachyos-desktop-linux-250828.iso
   ```
4. If the hashes from **Step 2** and **Step 3** match, you can proceed with the CachyOS installation.

<a id="cachyos-basic-download-verify-iso-image-authenticity-linux"></a>
### Verify ISO Image Authenticity (Linux)

To verify the authenticity of the ISO file and make sure that it’s the official one released by the CachyOS development team:

1. Import the GPG key for verifying the authenticity:

   ```shell
   gpg --keyserver hkps://keys.openpgp.org --recv-key F3B607488DB35A47
   ```

2. Download the ISO file and its [.sig](https://cdn77.cachyos.org/ISO/desktop/250828/cachyos-desktop-linux-250828.iso.sig) signature file and run the following command (by replacing `full_iso_name.iso` with the actual ISO filename):
   ```shell
   gpg --verify full_iso_name.iso.sig full_iso_name.iso
   ```

   If you get a **Good signature** output, the ISO file is genuine:
   ```
   gpg: Signature made jue 28 ago 2025 10:41:14 -03
   gpg:                using RSA key 882DCFE48E2051D48E2562ABF3B607488DB35A47
   gpg: Good signature from "CachyOS <admin@cachyos.org>" [unknown]
   gpg: WARNING: This key is not certified with a trusted signature!
   gpg:          There is no indication that the signature belongs to the owner.
   Primary key fingerprint: 882D CFE4 8E20 51D4 8E25  62AB F3B6 0748 8DB3 5A47
   ```

> **Danger:**
> If the output does not return a **Good signature** string or the key ID does not match, don't use the ISO image. Make sure that the downloaded image comes
> from a legitimate CachyOS source, since a bad signature could suggest that the ISO has been tampered with.

<a id="cachyos-basic-navigation-guide"></a>
#### How to navigate the CachyOS Wiki

Here are some tips to help you get the most out of the CachyOS wiki, including features that are easy to miss.

- **Contribute Feedback:**  If you have a suggestion or find an error in the documentation, you can help us improve!
- At the bottom of each page, you'll find an `Edit page` button that takes you directly to the corresponding file on GitHub where you can propose changes.
- Alternatively, you can open a new issue on our [GitHub repository.](https://github.com/CachyOS/wiki)
- **Search is Your First Tool:** Use the search bar at the top of the page (to the right of the CachyOS logo) to quickly find information related to your question or issue.
- **Navigate with the Sidebars:**
- The left sidebar is scrollable and contains the main table of contents for the entire documentation. Use it to explore different sections.

- Don't forget the right sidebar. It often contains a helpful overview of the current page's sections, allowing for quick navigation.
- **Look for Interactive Elements:**
- **Tabs:** Some pages use tabs to organize related content. Be sure to check all available tabs for the information you need.
- Example: ![Image](src/assets/images/tab-example.png)
- **Expandable Sections:** Content that is collapsed under a clickable header (like **"Manual Installation (Advanced)"**) can be expanded to reveal more detailed information.
- Example: ![Image](src/assets/images/summary-element-example.png)
- **Useful Features:**
- Code Blocks: All code blocks have a `Copy to clipboard` button on the top-right for easy copying.
- Example: ![Image](src/assets/images/code-block-example.png)
> **Note – Sometimes code blocks are used to show example output that doesn't need to be copied.:**
> - Hyperlinks: Keep an eye out for underlined and/or colored text. These are links to other parts of the wiki or external resources for further reading.
> - Pay close attention to notes, tips, warnings, and cautions. They contain important information that can help you avoid common pitfalls and solve problems faster.
> - Example: ![Image](src/assets/images/note-example.png)

<a id="cachyos-basic-why-cachyos"></a>
#### Why CachyOS?

CachyOS is a performance-centric Arch Linux distribution designed to deliver a stable, efficient, and user-friendly computing environment. It offers the full power and flexibility of a rolling-release system, enhanced by advanced optimizations and a custom toolchain that streamlines the user experience for both new and experienced users.

<a id="cachyos-basic-why-cachyos-performance-and-optimization"></a>
### Performance and Optimization

<a id="cachyos-basic-why-cachyos-optimized-packages-and-repositories"></a>
#### Optimized Packages and Repositories

CachyOS provides a large selection of **[optimized packages](https://packages.cachyos.org/)** specifically compiled for various modern CPU architectures. This includes support for `x86-64-v3`, `x86-64-v4`, and `Zen4+` systems, ensuring your software is built to take full advantage of your hardware's capabilities for a significant performance boost.

For a more in depth look of our optimized repositories, see our detailed guide on **[Optimized Repositories](#features-optimized-repos)**.

<a id="cachyos-basic-why-cachyos-custom-kernel-tuned-for-performance-and-stability"></a>
#### Custom Kernel Tuned for Performance and Stability

Aside from the CachyOS base kernel patch set that tunes various kernel parameters to improve desktop responsiveness, CachyOS cherry-picks patch sets that have not been mainlined or are not included in the stable revision of the kernel.

Therefore, these patches undergo internal testing before being released to users to ensure that stability isn't impacted. For a complete list of the patches that CachyOS provides, see [Kernel](#features-kernel).

<a id="cachyos-basic-why-cachyos-advanced-cpu-scheduler-support"></a>
#### Advanced CPU Scheduler Support

CachyOS ships kernels with the latest CPU scheduler optimizations to ensure a smooth and interactive desktop, even under heavy load.

* **EEVDF (The default Linux kernel scheduler):** While excellent for general throughput, the CachyOS kernel includes custom **[EEVDF tunables](https://github.com/CachyOS/linux/blob/6.15/cachy/kernel/sched/fair.c#L79-81)** to improve desktop responsiveness.

* **[BORE](https://github.com/firelzrd/bore-scheduler) (Burst-Oriented Response Enhancer):** For users who need maximum interactivity, our kernels support the BORE scheduler, a patch set that enhances EEVDF to deliver a more fluid experience during intensive workloads.

For more information about the kernels offered by CachyOS and the sched-ext framework, see the **[Kernel](#features-kernel)** and **[sched-ext](#configuration-sched-ext)** documentation.

<a id="cachyos-basic-why-cachyos-user-friendly-tools-and-customization"></a>
### User-Friendly Tools and Customization

<a id="cachyos-basic-why-cachyos-automated-hardware-detectionfeatures-chwd-chwd"></a>
#### [Automated Hardware Detection](#features-chwd-chwd)

CachyOS includes a custom hardware detection tool that automatically identifies and installs the necessary drivers and packages for your system. This eliminates the need for manual driver searching, saving you time and effort after installation.

<a id="cachyos-basic-why-cachyos-customizable-installation-process"></a>
#### Customizable Installation Process

The CachyOS installer lets users customize their system by choosing the desktop environment, packages, filesystem, boot manager, kernel, and more to fit their needs:

- [Desktop Environments](#installation-desktop-environments)
- [Boot Managers](#installation-boot-managers)
- [Kernel Flavors](#features-kernel-variants)
- [Filesystems](#installation-filesystem)
- [Custom Packages to include during installation](https://github.com/CachyOS/cachyos-calamares/blob/cachyos-limine-qt6/src/modules/netinstall/netinstall.yaml)

<a id="cachyos-basic-why-cachyos-cachyos-custom-applications"></a>
#### CachyOS Custom Applications

CachyOS develops and maintains its own suite of applications to simplify system management and enhance your experience.

List of applications that CachyOS currently develops and maintains:

-   **[CachyOS Hello](https://github.com/CachyOS/CachyOS-Welcome):** A welcome application for controlling tweaks, applying fixes, and installing packages.
-   **[CachyOS Package Installer](https://github.com/CachyOS/packageinstaller):** A graphical user interface (GUI) for easy installation of applications.
-   **[CachyOS Kernel Manager](https://github.com/CachyOS/kernel-manager):** Easily install kernels from the repository, configure your own, and manage the `sched-ext` framework.
-   **[cachyos-rate-mirrors](https://github.com/CachyOS/rate-mirrors):** Automatically ranks Arch and CachyOS mirrors for optimal download speeds with `pacman`.
-   **[systemd-boot-manager](https://github.com/CachyOS/systemd-boot-manager):** Automatically generates new boot entries for `systemd-boot`, which can be easily configured via `/etc/sdboot-manage.conf`.

<a id="cachyos-basic-why-cachyos-a-friendly-and-active-community"></a>
### A Friendly and Active Community

The greatest strength of CachyOS is its expanding community. Community members help one another by sharing tips, providing support, and contributing to the project's success. Your feedback helps us to continuously improve the CachyOS experience.

Join us and become a part of the community on the **[CachyOS Discord](https://discord.com/invite/cachyos-862292009423470592)** and the **[CachyOS Forum](https://discuss.cachyos.org/)**.

<a id="cachyos-basic-changelogs"></a>
### Changelogs

<a id="cachyos-basic-changelogs-cli-installer"></a>
##### CLI Installer

<a id="cachyos-basic-changelogs-cli-installer-084"></a>
## 0.8.4

<a id="cachyos-basic-changelogs-cli-installer-features"></a>
### Features ✨

- **Improved Partition Handling:**  Significant refactoring and improvements have been made to how the installer handles partitions, leading to better accuracy and reliability.
- **Kernel Parameter Generation:** The installer now automatically generates kernel parameters based on the detected partition scheme.
- **Enhanced `gucc` Library:**  The `gucc` library has been significantly enhanced, now encompassing refind installation and configuration capabilities.

<a id="cachyos-basic-changelogs-cli-installer-chores"></a>
### Chores 🧹

- **Clang-Format and Clang-Tidy:** Codebase consistency and quality have been improved through the application of clang-format and clang-tidy.
- **Refactoring with String Views:**  Several areas of the codebase now utilize string_view literals for improved performance and readability.
- **Doctest Implementation:**  C asserts have been replaced with doctest for more robust and informative testing.
- **Refactored Tests:** Test suites have been refactored for clarity and maintainability.
- **Refind Handling in `gucc`:**  Refind-related code has been refactored and moved into the `gucc` library for better organization and maintainability.

<a id="cachyos-basic-changelogs-cli-installer-bug-fixes"></a>
### Bug Fixes 🐛

- **Btrfs Subvolume Detection:** Issues with detecting existing btrfs subvolumes have been resolved.
- **Partition Information Accuracy:** Improvements have been made to ensure the accurate collection and display of partition information.
- **Root Mount Point for Refind:**  A bug affecting the root mount point used by refind has been fixed.
- **UUID Detection:** The process of detecting partition UUIDs during initialization has been improved.
- **Meson Build Fixes:**  Issues encountered during the meson build process have been addressed.
- **Btrfs Subvolume Appending:**  A bug related to appending btrfs subvolumes in development environments has been fixed.
- **Rootfs in Predefined Configurations:**  An issue with the rootfs of partition schemes derived from predefined configurations has been resolved.
- **Refind Read-Write Mounting:**  Ensured that refind mounts the necessary partitions with read-write permissions.

<a id="cachyos-basic-changelogs-cli-installer-083"></a>
## 0.8.3

<a id="cachyos-basic-changelogs-cli-installer-chores"></a>
### Chores 🧹

- Updated the CPR dependency to a newer version for improved functionality.
- Explicitly instructed CTRE (Compile Time Regular Expressions library) to utilize the C++23 standard for consistency and potential performance enhancements.
- Increased the connection check timeout in the utilities section to accommodate potential network delays or slow responses.

<a id="cachyos-basic-changelogs-cli-installer-082"></a>
## 0.8.2

<a id="cachyos-basic-changelogs-cli-installer-fixes"></a>
### Fixes 🐛

- Resolved an issue where "gucc" didn't correctly handle btrfs subvolume mountpoints.
- Improved "gucc" to handle different btrfs subvolume mount statuses.

<a id="cachyos-basic-changelogs-cli-installer-chores"></a>
### Chores 🧹

- Fixed a typo in the README file and updated the version information.

<a id="cachyos-basic-changelogs-cli-installer-081"></a>
## 0.8.1

<a id="cachyos-basic-changelogs-cli-installer-fixes"></a>
### Fixes 🐛

- Resolved an issue where ISA repos were incorrectly enabled on Oracle VM.
- Addressed command style inconsistencies for improved user experience.

<a id="cachyos-basic-changelogs-cli-installer-chores"></a>
### Chores 🧹

- Removed unnecessary ucode logic related to refind, streamlining the codebase.

<a id="cachyos-basic-changelogs-cli-installer-080"></a>
## 0.8.0

<a id="cachyos-basic-changelogs-cli-installer-features"></a>
### Features ✨

- Added parser for network package profiles.
- Introduced the ability to fetch environment packages from a TOML file parsed by gucc.
- Implemented a helper function in gucc to download files from URLs 📥.
- Added support for fetching network profiles from a URL with a fallback mechanism within gucc.
- Integrated the installation of network profiles with the binary distribution.
- Moved the mounting of specified partitions and detection logic into gucc.
- Introduced `utils::exec_checked` for safer execution of external commands.

<a id="cachyos-basic-changelogs-cli-installer-improvements"></a>
### Improvements ✅

- Enhanced test coverage for crypttab functionality in gucc 🧪.
- Improved logging in gucc by setting up the logger appropriately.
- **Updated C++ version to C++23** ⬆️.
- Refactored codebase to utilize C++23 features like `std::ranges` and `contains` for better readability and efficiency.
- Refactored various components to utilize `utils::exec_checked`.

<a id="cachyos-basic-changelogs-cli-installer-fixes"></a>
### Fixes 🐛

- Resolved an issue with hardcoded library types in gucc.
- Addressed missing logger implementation and header file in gucc.
- Enabled CPR library for non-development environment builds.
- Fixed static build process.
- Addressed issues introduced in commit [`a70e641e364`](https://github.com/CachyOS/New-Cli-Installer/commit/a70e641e364).
- Fixed compilation errors in the TUI component.
- Corrected a dependency issue where FTXUI's dependency on range-v3 was not public.

<a id="cachyos-basic-changelogs-cli-installer-chores"></a>
### Chores 🧹

- Updated CI checks, build processes, and fixed related issues.
- Removed the reverted installation of network profiles alongside the binary distribution.
- Refactored and cleaned up code in various components: TUI, utils, chwd_profiles, user, and tests.
- Removed the unused range-v3 library from installer dependencies.
- Updated README file.

<a id="cachyos-basic-changelogs-gui-installer"></a>
##### GUI Installer

25.08
----

**Features:**

* **Services:** Added **packages.cachyos.org**, a package search equivalent to Arch Linux’s website, with an option to exclude CachyOS packages.
* **Kernel:** The installer now additionally installs **linux-cachyos-lts** as a secondary/backup kernel after installation. We still recommend using the Stable kernel.
* **ISO:** Switched the live ISO’s kernel from Stable to LTS due to ongoing issues with the Stable kernel, improving boot reliability.
* **Desktop:** Added **Niri** as a desktop option, including a few preconfigured dotfiles.
* **NVIDIA:** Enabled **S0ix** sleep on supported hardware for modern low-power standby.
* **GRUB:** Bootable snapshots are now automatically enabled and set up when the root filesystem uses **Btrfs**.
* **Tweaks:** Integrated **Cachy-Update** into the Welcome app’s Tweaks page. Cachy-Update adds a timer and a system tray indicator to notify users about updates and lets them update with a click.
* **Proton-CachyOS:**
- Added downloader for DLSS dlls (version **310.3.0**), similar to the FSR4 downloader. Use `PROTON_DLSS_UPGRADE=1` environment variable to enable it.
- Added `PROTON_DLSS_INDICATOR=1` environment variable to enable DLSS hud.
- Added downloader for XeSS dlls (version **2.1.0**), similar to the DLSS downloader. Use `PROTON_XESS_UPGRADE=1` environment variable to enable it.
- Added `PROTON_FSR4_RDNA3_UPGRADE` for RDNA3 GPUs. Does the same thing as `PROTON_FSR4_UPGRADE` but also sets some other necessary variables.
- Added completer implementations of Nvidia libraries missing from Proton. Should help with enabling options such as PhysX on games they were disabled before. You can also enable them individually using `PROTON_NVIDIA_NVCUDA`, `PROTON_NVIDIA_NVENC`, `PROTON_NVIDIA_NVML` and `PROTON_NVIDIA_NVOPTIX`.
- Added per-game shader cache, enabled by default, can be disabled with `PROTON_LOCAL_SHADER_CACHE=0`. Shaders will be cached under `&lt;steamlibrary&gt;/shadercache/&lt;appid&gt;` for each game, similarly to when shader pre-caching is enabled. You will get stuttering as the shader cache for each game is rebuilt but the cached shaders won't be evicted due to limited cache size.
- Added [dxvk-sarek](https://github.com/pythonlover02/DXVK-Sarek) as an optional DXVK replacement for older GPUs that don't properly support Vulkan 1.3. It is using the `async` branch, so it SHOULD NOT to be used with games using anti-cheat or multiplayer games in general. You have been warned. Use `PROTON_DXVK_SAREK=1` to enable.
- Added `PROTON_FSR3_UPGRADE` to upgrade FSR 3.1 DLLs to newer versions.

**Fixes:**

* **Limine:** 
- Fixed `limine bios-install /dev/sdaX` error when selecting the **/boot** mount point as the boot location on MBR systems.
- Fixed uninitialized value of the `bootLoader` path, which caused installation failures on MBR systems when the bootloader location wasn’t explicitly selected.
- Added a warning about using the **bios-grub** flag on the boot partition, which can cause a “Stage 3 file not found” error.
- Fixed out-of-the-box dual-boot with Windows for BIOS installations.
- Fixed Btrfs snapshots failing to boot when using **GNOME (GDM)**.
* **Launch Installer:** Added fallback IPs for the online check if pinging **cachyos.org** fails.

25.07
----

**Features:**

- **Shell**: The user shell can now be chosen at installation time between fish, zsh and bash. Fish stays enabled by default.
- **chwd**: Install plasma-x11 for legacy NVIDIA Drivers
- **Netinstall**: Added fwupd to KDE Plasma and Gnome
- **mesa-git**: Added support for AMD Anti Lag
- **firefox**: Introduced an alternative firefox called "firefox-pure", which includes improvement with the userjs profile. Additionally, there has been "cachyos-firefox-settings" added, which can be installed on top of firefox.
- **Proton-CachyOS**:
- Imported upstream wine-wayland commits
- Added "PROTON_FSR4_UPGRADE" env variable, which will automatically download the latest FSR4 DLL and then replace it for an automatic upgrade on FSR 3.1 supported games
- Added many Wayland-related patches from upstream Wine that were released after Wine 10.0.
- added patches to help with better anticheat integration. Thanks to NelloKudo
- Added patches for AMD's Anti Lag 2 for vkd3d-proton and wine
- Updated umu-protonfixes to latest commit

**Fixes:**

- **Keyring**: Improved the handling of the keyring installation to avoid issues and do several retries.
- **systemd-oomd**: Disabled systemd-oomd, since it had problems handling this together with le9 and killed applications way to early

**Changelog for Handheld Edition:**

- **handheld-settings**: Imported several tweaks of SteamOS to the Handheld Edition
- **pipewire**: Set minimum quantum to 256
- **SteamDeck-OLED**: Install galileo-mura for Steam Deck OLED
- **Lenovo Legion Go S**: Added support for the Lenovo Legion Go S

25.05
----

**Features:**

- **ISO**: Added automatic detection during ISO boot to identify the system's NVIDIA GPU and load the appropriate module (e.g., nvidia-open, nvidia), providing better support for 10xx series and older.
- **Plymouth**: Added a new Plymouth animation.
- Thanks to Eren ([https://github.com/erenyldz89](https://github.com/erenyldz89)) for working on this!
- **Browser**: Cachy-Browser has been deprecated. We now provide Firefox as the default preinstalled browser. A guide to migrate profiles to Firefox (and its forks) can be found here: [https://wiki.cachyos.org/support/faq/#migrating-your-profile-from-cachy-browser-to-firefox](https://wiki.cachyos.org/support/faq/#migrating-your-profile-from-cachy-browser-to-firefox)
- **netinstall**: Added kcalc, filelight, plymouth-kcm, and kio-admin to the KDE installation.
- **mkinitcpio**: Disabled fallback initramfs by default. This will save a significant amount of space.
- **Mirrors**: Added a new 10 Gbps mirror in Bangladesh. Thanks to Limda for hosting this!
- **Proton**:
- Rebased almost all patches from **Proton CachyOS 9.0**.
- Enabled the Wayland driver for Steam Linux Runtime builds. Enable with `PROTON_ENABLE_WAYLAND=1`. Thanks to [GloriousEggroll](https://github.com/GloriousEggroll) for making it happen.
- Added many Wayland-related patches from upstream Wine that were released after Wine 10.0.
- Fixed various issues with the Wayland driver and Vulkan games. Thanks to [Etaash-mathamsetty](https://github.com/Etaash-mathamsetty) for all the hard work.
- Added a stub implementation for `amdxc64.dll` to enable FSR4. Use `FSR4_UPGRADE=1` to upgrade FSR3.1 games to FSR4. Thanks again to [Etaash-mathamsetty](https://github.com/Etaash-mathamsetty). Instructions: [https://github.com/Etaash-mathamsetty/wine-builds/releases/tag/fsr4](https://github.com/Etaash-mathamsetty/wine-builds/releases/tag/fsr4)
- Added DualSense-related patches for more complete audio device detection functionality for wired sound-based haptics. Some games that relied on that specific behaviour should now have that functionality. Thanks to [ClearlyClaire](https://github.com/ClearlyClaire) for the original patches and [Exotic0015](https://github.com/Exotic0015) for looking into it since **Proton CachyOS 9.0**. Upstream: [https://gitlab.winehq.org/wine/wine/-/merge_requests/7238](https://gitlab.winehq.org/wine/wine/-/merge_requests/7238)
- Removed the Dragon Age Inquisition patch as it was not working. Please use **Proton CachyOS 9.0** for now with that game.
- **GRUB**: Added a new GRUB theme. Thanks to [diegons490](https://github.com/diegons490/cachyos-grub-theme).

**Fixes:**

- **Mirrors**: Fixed an issue where users from Russia could no longer install. This was mitigated by not using CDN77, which Russia had started to block.
- **kde-settings**: Disabled the Discover icon in the taskbar.
- **ddcutil**: Pushed the ddcutil 2.2.1 pre-release to fix an issue where AMD GPUs were freezing when watching YouTube videos.

**Changelog for Handheld Edition:**

- **os-branch**: Game Mode now correctly shows that CachyOS Linux is being used.
- **audio**: Updated convolver profiles.
- **steamos-manager**: This is used for GPU clock and TDP management, BIOS/dock updates, storage device maintenance, external storage formatting, and battery charge limit for the Steam Deck.
- **steamos-powerbuttond**: This component replaces the standard powerbuttond for a better sleep experience.
- **jupiter-hw-support**: Updated to 20250501.

25.04
----

**Features:**

- **occt**: Added OCCT to the ISO to have a live environment for stress testing
- Thanks to Marek for providing this idea!

**Fixes:**

- **kernel**: Fixes module crash on Asus laptops
- **limine**: Limine now has mkinitcpio-limine-hook installed and will automatically create bootloader entries

**Changelog for Handheld Edition:**

- **audio**: Added audio profiles for ROG Ally X and Legion Go
- **gamescope**: Replaced gamescope-plus with upstream gamescope

25.03
----

**Features**:

- **Bootloader**: Added support for Limine bootloader
- **Bootloader**: Added support for automatic snapshots for Limine bootloader
- **Samba**: Added "cachyos-samba-settings" package to easily set up a Samba mount
- **NVIDIA**: Re-enabled GSP Firmware for the closed source NVIDIA module
- **Kernel**: Added support for the Asus Armoury driver
- **Secure Boot**: Improved "sbctl-batch-sign" script to sign only wanted files
- **udev**: Reverted using ntfs3 as the default driver for NTFS partitions
- Info: Using the NTFS3 Kernel driver as default resulted in issues for some users. Therefore, we reverted it again.
- **wine**: Wine and Wine-Staging defaulting now to WoW64 and NTSync
- **scx-manager**: Moved out sched-ext GUI manager from Kernel Manager to its own application
- **Hardware Support**: Added support for RDNA4, RTX 5070 Ti, and 5070.
- **Settings**: Added DLSS Swapper Support - this is a script, which automatically updates and uses the latest dlss version and preset
- **Package Updates**: linux-cachyos 6.14.0, NVIDIA 570.133.07, Gnome 48, Plasma 6.3.3, mesa 25.0.2, linux-api-headers 6.14.0, linux-tools 6.14.0

**Fixes**:

- **initcpiocfg**: Removed "crc32c-intel" module adding to mkinitcpio - This has been deprecated and now defaults to the "crc32c" module
- **chwd**: T2 MacBook disable offloading the brcmfmac
- **chwd**: Do not install NVIDIA 390.xx driver for laptops

25.02
----

**Features**:

- **Kernel**:
- Propeller Optimization is now applied to the default **linux-cachyos** kernel for all available architectures.
- **Note**: In combination with AutoFDO, this can improve performance by around 10%, depending on the workload.
- **NVIDIA**: Added support for the Blackwell Architecture.
- **ISO**: Using the nvidia-open module as the default to provide Blackwell support. Users with GPUs older than Turing should use the first or fallback boot option.
- **Settings**: Enabled tap-to-click for X11 sessions by default.
- **udev**: Use ntfs3 as the default driver for NTFS partitions.
- **game-performance**: Disabled the screensaver while running games.
- **kernel-manager (sched-ext)**: Added support for server mode.
- **kernel**: Added fixes for the AMD preferred core feature.
- **chwd**: Re-added the workaround for RTD3.
- **Package Updates**: linux-cachyos 6.13.0, NVIDIA 570.86.16, LLVM 19, glibc 2.41, mesa 24.3.4.

**Fixes**:

- **chwd**: Fixed an issue where hybrid laptops with Intel and NVIDIA hardware could not use their GPU in DaVinci Resolve.
- **glibc**: Added a fix for CVE-2025-0395.
- **kernel-manager**: Attempted to install the prebuilt NVIDIA module, if available for the default Arch kernel.
- **kernel-manager**: Added an extra check to avoid overwriting the value in case a module is not available.

**Changelog for Handheld Edition:**

- **hooks**: Allowed the use of natively compiled Proton again.
- **misc**: Several updates and fixes.

24.12
----

**Features**:

- Kernel:
- AutoFDO is now applied to the default `linux-cachyos` kernel for all available architectures
- **Note**: Performance improvements are minimal for now due to current limitations. Merging profiles requires LLVM 19, and Propeller Optimization depends on it. We anticipate LLVM 19 and more optimized profiles to be available by the end of the year, following Arch Linux's adoption of LLVM 19
- chwd: Rusticl is now configured correctly
- chwd: improved error logging during hooks calls
- chwd: fixed VAAPI drivers selection
- cachyos-settings: Added a script to facilitate running applications via Zink
- Sysctl Configuration: Reworked and optimized several settings
- Kernel Manager: Added support for `scx_loader`, enabling native scheduler switching
- Installer: Bluetooth service is now enabled by default
- Netinstall:
- Added `wireless-regdb` to the installed packages
- This configures the connection to use appropriate channels and unlocks additional channels, potentially improving internet speed
- **Note**: A generic region is set by default; customizing it to your region is recommended for optimal performance
- **Package Updates**: NVIDIA 565.77, linux-cachyos 6.12.6, mesa 24.3.2, scx-scheds 1.0.8, zfs 2.2.7

**Bug Fixes**

- Installer: Installation logs no longer spawn debug terminal windows
- Partition Management:
- Proper `umask` settings ensure `/boot` is inaccessible without sufficient permissions
- Launch Installer: Internet connectivity checks have been fixed

**Changelog Handheld Edition:**

- Updated handheld related packages
- Fixed issue with the power profile handling
- Added support for WiFi 6

24.11
----

**Features:**

- thp-shrinker: Put max_ptes_none value to 80% for zero filled pages. This will reduce the memory usage for when THP always is used, while maintaining the same performance
- NVIDIA: GSP Firmware gets now automatically disabled, if the users switches on their own to the closed driver
- chwd: NVIDIA: nvidia-powerd services gets enabled for laptops, to reach the most available tdp
- proton-cachyos: DLSS Frame Generation is now working. This is also expected to work in the future in the upstream proton
- kernel: AMD Cache Optimizer is now applied. Users with dual x3d CCD's cpus can now switch between having frequency or cache cores preferred
- kernel: amd-pstate: Backported amd-pstate performance fixes for Strix Point
- kernel: Added upstream fixes for the tdp issues on amd rdna2 and rdna3 gpus
- kernel: Added timing fixes for displays with 5120x1440x240 configuration
- kernel: Experimental AutoFDO optimized kernel in the repository under "linux-cachyos-autofdo"
- ISO: Added check, if user running handheld edition and warn then, if they are starting the installation on an unsupported device
- ISO: Added check, if the user is using the latest ISO, if not warn them

**Bug Fixes:**

- refind: partitioning: changed from 3 way partiton layout to 2 way
- netinstall: added kdeplasma-addons to the Plasma installation
- calamares: Fixed an issue, while partitioning with a swap partition

**Changelog Handheld Edition:**

- Rog Ally X Support should have been improved

24.10
----

**Features:**

- Package Updates: linux-cachyos 6.11.1, mesa 24.2.4, scx-scheds 1.0.5, python 3.12.7

**Bug Fixes:**

- sddm: Pulled in newer sddm to fix wayland session logins
- ISO: Added xf86-video-amdgpu to fix graphical session loading on some setups
- chwd: Fixed reinstallation of profiles

24.09
----

**Features:**

- Packages: Optimized a bunch of packages with PGO, like LLVM, Clang, svt-av1, and nodejs. This yielded, for example, a 10% faster Clang compiler
- Repository: The repository is now synced and updated more frequently, meaning there will be even less delay. The sync interval has been decreased from every 3 hours to every hour.
- Repository: Starting from 27.09.2024, packages compiled with -fpic will automatically enable -fno-semantic-interposition. This can provide a performance improvement for many packages.
- zlib-ng: Is now used as a replacement for zlib
- sddm: On the KDE Installation, sddm will now default to Wayland as the compositor. # Provide Migration changes in release post
- cachyos-settings: NetworkManager now uses systemd-resolved as the backend, which helps with DNS caching
- cachyos-settings: Use time.google.com as the timesync server to avoid issues with timesync on some setups
- gcc: Added fixes for the tuning of znver5
- gcc: Cherry-picked patches and flags from Clear Linux
- glibc: Added "evex" patches as well as cherry-picks from Clear Linux
- wiki: The Wiki received many new additions and reworks
- chwd: Simplified device handling
- chwd: All profiles are now specifically designed for PCI devices
- chwd: Add --autoconfigure to automatically handle the driver installation
- Package Updates: linux-cachyos 6.11.0, mesa 24.2.3, Plasma 6.1.5, NVIDIA 560.35.03, calamares 3.3.10, QT 6.7.3

**Bug Fixes:**

- Launch-Installer: Added fixes to sync the hardware clock before starting the installation
- calamares: Added fix for unmounting the filesystem after installation
- keyring: Clean up the keyring and recreate it before starting installation; this fixes rare keyring issues
- sysctl: Core dumps have been enabled again
- chwd: Removed `libva-nvidia-driver` from the PRIME profile to prevent potential conflicts and improve compatibility with software like Spectacle
- cachyos-settings: Added workaround for GNOME Wayland crashes
- cachyos-fish/zsh-config: Dropped wayland specific quirks

**Changelog for Handheld Edition:**

- Ally/Ally X: HHD got replaced with inputplumber, since hhd does not use the kernel driver for it correctly, which results in issues.
- Handheld related packages updated

24.08
----

**Features:**

- chwd: NVIDIA now uses the open module as default for supported cards
- Desktop: Added Cosmic Desktop Environment to the installation options
- NVIDIA: Latest 560 Beta driver is now the default; egl-wayland patched to fix crashes in Firefox and other applications
- mirrors: CDN77 sponsored CachyOS with Object Storage featuring a worldwide cache, significantly improving connection speeds for users
- mirrors: CachyOS now provides its own Arch Linux mirror to avoid syncing issues, set as default during installation along with fallback mirrors
- SecureBoot: Introduced script and tutorial in the Wiki for easy Secure Boot support
- cachy-chroot: Added auto-mount via fstab for simplified chrooting
- cachy-chroot: Implemented support for LUKS Encryption
- kernel-manager: Added support for setting sched-ext flags in the sched-ext configuration
- kernel-manager: Introduced option to build nvidia-open
- kernel-manager: Added option to remember last used options in configure page
- Package Updates: linux-cachyos 6.10.5, mesa 24.2.0, Plasma 6.1.4, NVIDIA 560.31.02

**Bug Fixes:**

- chwd: Improved PRIME profile detection based on device name
- chwd: Removed RTD3 workaround due to issues on some setups
- cachyos-rate-mirrors: Disabled mirror ranking when running on Live ISO
- cachy-chroot: Fixes a crash when a partition didn't have a valid fstype or uuid (eg Microsoft Recovery Partition)
- calamares: Refactored keyring initialization
- kernel-manager: Fixed support for building custom pkgbase with LTO kernels and modules enabled
- kernel-manager: Fixed password prompt delay
- ISO: Replaced radeon.modeset=1 with amdgpu.modeset=1 for modern GPUs
- game-performance: Prevented failure when profile is unavailable

**Changelog for Handheld Edition:**

- device support: Added support for Ally X, thanks to Luke Jones
- libei: Implemented support for libei, replacing libextest
- packagekit: Blocked packagekit installation to prevent issues with system updates via Discover
- hook: Added pacman-hook to conflict with natively compiled Proton versions, avoiding potential issues
- Updated jupiter-fan-control, steamdeck-dsp, and Steam Deck firmware

24.07
----

**Features:**

- Repository: Introduce Zen 4 optimized repository, this will be used for Zen4 and Zen5 CPU's
- ISO: Add automatic architecture check for Zen4/Zen5 repository
- chwd: Added GC support for AMD GPU's, this helps for detecting official ROCm supported GPUs
- chwd: Use libva-nvidia-driver on supported cards
- ksmctl: Introduce tool to enable/disable KSM: ksmctl --enable
- kernel: For the "linux-cachyos" kernel is now a "linux-cachyos-dbg" package available, this contains an unstripped vmlinux for debugging purposes
- kernel: amd cpb boost is now available and the power-profiles-daemon is patched, if the "powersave" profile is set, it will disable the boost on amd cpus
- kernel: Added power saving patch for AMD SoCs for video playback
- kernel-manager: Added support for managing sched-ext schedulers and getting information via GUI
- steam/proton: There is now a "game-performance" script, which can be added to steam's launch options
- power-profiles: On AMD Pstate supported CPUs the lowest Linear frequency is now set higher, this can improve latency and 1% lows
- kwin: Added back-port for tearing, this has been tested. On NVIDIA, it only works on native wayland applications
- netinstall: Cutefish has been dropped as installable Desktop Environment
- Mirrors: Added Austria and China Mirror, the China Mirror is hosted by the TUNA University. This should help a lot of users from China
- Package Updates: linux-cachyos 6.9.9, mesa 24.1.3, NVIDIA 555.58.02, Plasma 6.1.2, LLVM 18.1.8

**Bug Fixes:**

- ISO: Set copytoram to auto instead of yes
- ISO: Fixed Sleep on Live ISO for Laptops
- Launch Installer: Install the latest archlinux-keyring, before the installation starts to avoid issues, when fetching the archlinux-keyring in the chroot
- Mirrors Ranking: Rank only Tier 1 Mirror's at installation time
- pacman.conf: Remove not used pacman repository
- cachy-chroot: Do not show .snapshot subvolumes
- Calamares: Do not use "Preservefiles" module, since user a reporting issues with it.

**Changelog for Handheld Edition:**

- Added configuration file to apply different scaling, '/home/$USER/.config/deckscale
- Make GameMode switching more robust
- Updated Wifi/Bluetooth Firmware for Steam Deck
- Implemented Auto Mount for GameMode
- Added gamescope-session quirks for Wine CPU Topology, HDR, and Backlight
- Fixed Refresh Rate Selection
- Updated jupiter-hw-support, steamdeck-dsp, jupiter-fan-control, gamescope-session-git

24.06
----

**Features:**

- chwd: Introduce handheld hardware detection
- chwd: Introduce T2 MacBook support
- chwd: Add network driver detection
- Installation: Added MacBook T2 support
- ISO: Add cachy-chroot. This is a script that helps the user to chroot into the system.
- ISO: Switch to Microcode Hooks; this requires using the latest Ventoy release (1.0.98)
- ISO: Enable copytoram; this no longer needs to be disabled because we don't provide the offline installation anymore
- filesystem: BTRFS is now the default selected file system
- netinstall: Use ufw instead of firewalld
- Calamares: Update Branding Slides
- Slides: Updated for latest changes
- Package Updates: linux-cachyos 6.9.3, mesa 24.1.1, xwayland 24.1, NVIDIA 555.52.04, Plasma 6.0.5

**Bug Fixes:**

- Calamares: umount: Enable emergency again
- Qtile: Multimedia Controls are now working correctly
- NVIDIA: Enable required services and options for working sleep on Wayland
- netinstall: Remove b43-fwcutter from installation
- netinstall: Replace hyprland-git with hyprland
- netinstall: Drop linux-cachyos-lts from selection to avoid issues with missing modules
- Calamares: Shellprocess: Move mirror ranking before installing keyring

**Changelog from Experimental Handheld Release:**

- Default to KDE Vapor Theme (SteamOS Theme)
- Default file system: BTRFS
- Default kernel: linux-cachyos-deckify
- SDDM now uses Wayland
- Environment Flag for HHD to reduce latency
- Added Kernel Arguments to improve Game Mode Switching behavior
- The username can now be edited
- Hardware Detection configures and installs required packages depending on the device used
- Mallit Keyboard now uses Dark Mode
- Valve's Powerbuttond for proper sleeping
- Shortcuts can now be added to Steam
- Updated scx-scheds to latest git commit, providing the latest enhancements for the LAVD Scheduler
- Added automount to cachyos-handheld
- CachyOS can now perform Steam Deck BIOS updates on the Steam Deck

24.05
----

**Features:**

- Filesystems: Introduce Bcachefs as a filesystem option
- pacstrap: Add detection if Bcachefs is used and install corresponding Bcachefs-tools
- CachyOS-AI-SDK: Introduce new install option to provide a OOB NVIDIA SDK Setup
- CachyOS-Deckify: Provide variant for Handhelds (experimental), see [here](https://discuss.cachyos.org/t/information-experimental-cachyos-deckify/203) for more details
- BTRFS: Automatic Snapper for snapshots, can be installed from within the CachyOS hello app.
- ISO: Drop Offline Installer
- Package Updates: Python 3.12, gcc 14.1.1, mesa 24.0.6, xwayland 24.1rc2, NVIDIA 550.78

**Bug-Fixes:**

- settings.conf: Move hardware detection before netinstall
- pacstrap: Use btrfs-assistant instead of btrfs-assistant-git
- plymouth: remove plymouth hook on zfs + encryption
- ISO: Add various config files for KDE, to avoid getting screen locking during installation
- services-systemd: Properly enable fstrim.timer
- umount: Disable emergency to avoid issues with the zfs installation
- shellprocess: Cleanup leftovers from the offline installation

24.04
----

**Features:**

- Plymouth: Use plymouth to provide a themed boot animation
- ISO: Switch back to X11 due to issues when setting the keyboard layout in calamares
- rEFInd: New partitioning layout (seperate /boot and /boot/efi)
- netinstall: KDE: Install xwaylandvideobridge by default
- netinstall: Use lightdm instead of ly for various Desktop Environments, due to a bug in ly
- systemd-boot: Use @saved for systemd-boot to allow it to remember the previously selected boot entry
- cachyos-keyring: Refactor cachyos-keyring package and provide a cachyos-trusted keyring
- ISO: Use ZSTD 19 Compression for the mkinitcpio image of the ISO
- Package Updates: xz 5.6.1-3, linux-cachyos 6.8.2, pacman 6.1.0-5, mesa 24.0.4, Plasma 6.0.3, nvidia 550.67 and cachyos-settings 39-2

**Bug-Fixes:**

- Autologin: Fixed the autologin option when used together with sddm
- xz: Provide a patched xz package
- libarchive: Mitigate commit from malicious xz actor
- cachyos-settings: udev-rule: don't set watermark_scale_factor to 125, since it siginificantly increases RAM usage
- calamares: pacman-keyring: Use simpler method to integrate the keyring into the installation

24.03.1
----

**Features:**

- netinstall: Remove extra kernels in the netinstall selection to avoid confusion by users. Other custom kernels can be installed via Kernel Manager
- Kernel Manager: NVIDIA Modules are automatically installed when detected, Rebased for QT6, Fixed custom names when using LTO Option
- Package Installer: Rebased on QT6, updated for pacman 6.1
- Package Updates: linux-cachyos 6.8.1, pacman 6.1, mesa 24.0.3, Plasma 6.0.2, llvm 17.0.6

**Bug-Fixes:**

- NVIDIA: patched nvidia module to take the ownership of nvidia.drm.modeset earlier to avoid issues on nvidia graphics
- Refind: Don't install the lts kernel to avoid issues
- shellprocess: Remove the liveusers directory completly

24.03
----

**Features:**

- ISO: Plasma 6 is now shipped in the ISO and uses Wayland as default, GNOME ISO got dropped to avoid confusion about netinstall
- Calamares: Rebased for QT6
- refind: Add f2fs and zfs as option including luks2 encryption
- mirrors: We provide now 2 global CDNs. One hosted by Cloudflare R2 and one hosted by Digital Ocean
- mirrorlist: Fetch the online installer directly from cdn to provide a faster delivery
- initcpiocfg: Use the new microcode hook for early loading the ucode
- bootloader: Dont load the microcode with the bootloader anymore
- Package Updates: linux-cachyos 6.7.9, mesa 24.0.2, zfs-utils 2.2.3

**Bug-Fixes:**

- pacstrap: Do not install config packages to provide the user a more clean selection of the installation
- shellprocess_pacman: Also copy the ranked cachyos-v4-mirrorlists to the target

24.02
-----

**Features:**

- refind: Change layout from /boot/efi to /boot to provide more options of filesystems and encryption
- Live-ISO: Cleanup and Sync the Live-ISO
- Launch Installer: Add recommendation for the online installation
- shell-configs: Add option to disable fastfetch when starting the terminal and add an "update" alias
- netinstall: Add phonon-qt5-vlc to kde
- Package Updates: linux-cachyos 6.7.5, mesa 23.3.5, gcc 13.2.1-12, glibc 2.39, mesa 24.0.1, nvidia 550.54.14

24.01
-----

**Features:**

- x86-64-v4: Autodetection and enabling the repository at installation
- linux-cachyos: the sched-ext scheduler framework is now provided in the default kernel
- xwayland: Provide explicit sync patches as default
- Package Updates: linux-cachyos 6.7, mesa 23.3.3, gcc 13.2.1-8, xorg-xwayland 23.2.4

**Bug Fixes:**

- chwd: For Ada Lovelace Nvidia cards the nvidia modules get directly packed into the initramfs to avoid issues with the early kms

23.12
-----

**Bug-fixes:**

- zfs: Add compatibility=grub to the pool options to ensure the compatibility
- grub/xfs: Add a patch to grub to have compatibility with the new xfs bigtime default
- netinstall: xdg-desktop-portal-hyprland instead of xdg-desktop-portal-hyprland-git

23.11
-----

**Features:**

- nvidia: Use nvidia module instead of dkms
- Calamares synced with upstream
- Package updates: linux-cachyos 6.6.1, nvidia-utils 545.29.02, mesa 23.2.1, zfs-utils 2.2.0, mkinitcpio 37

**Bug-fixes:**

- nvidia-hook: Added nvidia-hook back to avoid issues at installation time with the new module
- netinstall: Packages got renamed due the recent changes at the KF5 packaging
- netinstall: xdg-desktop-portal-gnome got added to the GNOME Installation

23.09
-----

**Features:**

- systemd-boot: Default to luks2
- netinstall: Provide a own category for CachyOS Packages
- Calamares synced with upstream
- Package updates: linux-cachyos 6.5.3, nvidia-utils 535.104.05, mesa 23.2.7

**Bug-fixes:**

- shellprocess_sdboot: Avoid using "sudo", when generating the boot entries at the installation process

23.08
-----

**Features:**

- Calamares synced with upstream
- Package updates: linux-cachyos 6.4.10, nvidia-utils 535.98

**Bug-fixes:**

- Keyring got updated and works now correctly

23.07
-----

**Features:**

- CachyOS-Settings includes now "bpftune", which automatically tweaks the network settings depending on the usage
- CachyOS-Qtile-Settings: Quality of Life changes, better icons, ...
- Package updates: linux-cachyos 6.4.2, cachy-browser 115.0.1, mesa 23.1.3,

**Bug-fixes:**

- rate-mirrors got fixed
- chwd (Hardware Detection) got multiple fixes
- fixed installation of nonfree drivers for hybrid setup in the installer
- fixed Calamares freezes, which happened in some rare configurations, mainly VM
- Slides: Slide 6 typo fix

23.06
-----

**Bug-fixes:**

- Offline Installation: Fix calamares

23.05
-----

**Features:**

- CachyOS Git Migration layout is now reflected in the installation
- chwd (mhwd) got multiple fixes
- Pacman: We added a feature, which makes it possible to provide a message to our users before updating
- Calamares got synced with upstream
- Package updates: linux-cachyos 6.3.4, cachy-browser 113.0.1, mesa 23.1.1, python 3.11

**Bug-fixes:**

- netinstall: minimal fixes due package changes
- Slides: Slide 6 got updated to reflect the lastest chang

23.04
-----

**Features:**

- Introduce the Qtile desktop enviroment
- Reworked mhwd: Rust rewrite; Simplified profiles for GPUs and network cards; Removed bunch of ancient code
- Package updates: linux-cachyos 6.2.12, cachy-browser 112.0.1, mesa 23.0.3, zfs-utils 2.1.11

**Bug-fixes:**

- f2fs: Remove "atgc" mount options since it has issues with systemd

23.03.1
-------

**Features:**

- Package updates: linux-cachyos 6.2.7, cachy-browser 111.0

**Bug-fixes:**

- Calamares got fixed with the lightdm displaymanager due faulty calamares upstream commits
- Offline installation keyring issue got fixed
- Refind: Use linux-cachyos-lts as defaullt. Current 6.2 seems not to work well together with refind

23.03
-----

**New Features:**

- Added the refind bootloader
- Automatic Nvidia driver installation using MHWD
- Encryption support for ZFS installation
- Added Hyprland to netinstallation
- CachyOS-KDE-Settings now uses the KDE default theme, but the CachyOS Themes are still preinstalled and available for use
- Package updates: linux-cachyos 6.2.2, mesa 23.0.0, cachy-browser 110.0.1, plasma 5.27.2
- Fully reworked and improved the bootloader calamares module
- The ISO gets now signed with a GPG key
- MHWD got improved and updated
- Synced Calamares with upstream

**Bug-fixes:**

- The "replace partition" option now offers a filesystem selection
- Fixed a typo in slide 3
- nouveau got fixed and does now proper load the module
- MHWD: Use modesetting for INTEL/ATI and Nouveau
- Removed the zfs hook from mkinitcpio on the live iso, which caused issues when booting
- You can download the update from our mirrors on SourceForge.

23.02
-----

**New Features:**

- The cachyos-community-v3 repo has been added
- Budgie, Mate, and LXDE desktop environments have been added to the Netinstallation
- Bluetooth.service is now enabled by default
- F2FS and grub are enabled and working again
- Package Updates: linux-cachyos 6.1.10, mesa 22.3.4, zfs-utils 2.1.9, glibc 2.37, cachy-browser 109.0.1

**Bug-fixes:**

- Rate-mirrors now fall back to unranked mirrors if it fails to rate them
- cachyos-rate-mirrors has a longer fetch-mirrors-timeout
- Github has been added to the hosts to avoid mirrorlist issues
- Boot entries for BIOS have been updated in syslinux

23.01
-----

**Features:**

- Calamares Slides got reworked and updated
- UKUI Desktop Enviroment got added to the Netinstallation
- Cinnamon Desktop Enviroment got added to the Netinstallation
- Cmdline: zswap is now disabled as default because CachyOS provides zram as default
- Calamares updated to the latest commit
- LLVM 15 is now shipped as default
- Package Updates: linux-cachyos 6.1.7, mesa 22.3.3, Plasma 5.26.5, llvm 15.0.7, gcc 12.1.1, binutils 2.40, zfs-utils 2.1.8, nvidia 525.85.05
- CLI Installer got updated

**Bug-fixes:**

- remove-ucode shellprocess does also run now at the offline installation
- pamac got removed from the netinstall
- The ranked cachyos mirrors gets now correctly copied to the install target
- power-profile-daemon don't gets enabled anymore as default

22.12
-----

**Features:**

- New GRUB background at the ISO bootloader
- memtest is now included for UEFI Systems
- CachyOS-sddm-theme got added to the KDE Installation
- Automatic version script added when creating the ISO
- Calamares updated to the latest commit
- The mirrors are now ranked with "cachyos-rate-mirros", which ranks our mirrors and the arch ones
- Packages Update: 6.1.1 Kernel, mesa 22.3.1, plasma 5.26.4,...
- The Kofuku Desktop Enviroment got removed
- extra ISO with llvm 15 included to provide support for newer AMD Cards

**Bug-fixes:**

- Calamares got fixed when using GNOME as ISO
- zfshostid does now work proper for the offline and online installation
- Add "kms" hook to the initcpiocfg module to follow archlinux defaults
- And more ISO fixes

22.11
-----

**Features:**

- Calamares and its config are shipped in one package
- Complete Cleanup of the packages in the netinstall
- Add a module which automatically removes the not needed ucode
- required RAM decreased to 2.5GB
- Packages which are required for btrfs, are now only installed for btrfs
- Calamares updated to the latest commit
- The ISO Bootloader has now a background
- Common package upgrades (mesa, kernel, ...)
- Replace systemd-network with networkmanager

**Bug-fixes:**

- qemu-quest-agent.service got removed from the ISO
- copytoram got completly disabled, it breaks the offline installation
- mkinitcpio.conf got updated
- And more ISO fixes

22.10
-----

**Features:**

- Pacman uses now Architecture=auto for x86-64-v3 installation, since we added a patch that pacman does autodetect x86-64-v3
- Pacman does show now, from which repo a package was installed
- Bootloader selection auto detect if EFI is present, if not it will default to grub
- Swap choice has been disabled now as default, since zram gets automatically dynamically generated
- Calamares updated to the latest commit
- Minimum RAM requirement has been set to 4GB
- cachyos-grub-theme got removed

**Bug-fixes:**

- SSD and hdd fstab detection has been disabled until there is a upstream fix
- double BTRFS subvolume has been fixed
- Added missing microcode to the ISO grub bootloader
- Added a fallback bootmode, which does not set any modeset (nomodeset)
- And more ISO fixes

22.09
-----

**Features:**

- Calamares is now on the latest 3.3 branch. Its brings bugfixes and new features to calamares
- TUI-Installer is now included in the GUI ISO, you can use it with "cachyos-installer"
- Calamares does now auto detect, if the target filesystem is a ssd or hdd and adjust to it the fstab options
- Nvidia for latest gpu's (starting at 9xx) has now a own boot entry, to avoid issues with nouveau
- fstab and zfs mount options got updated
- FireFox won't be installed as default anymore since cachy-browser is installed as default

**Bug-fixes:**

- cachyos-gaming-meta has been removed from the netinstall module to avoid issues at the installation process
- netinstall packages has been updated and got some fixes
- OpenBox installation has been fixed
- usual translation fixes

22.07
-----

**Features:**

- Boot-loader selection: User can now choose on the online installation between grub and systemd-boot
- At online installation will now always the newest calamares installed, which helps to do bug fixes on the "air"
- Calamares has now a mhwd module which automatically installs the needed drivers (free drivers)
- Calamares has new picture slides at the installation
- fstab and zfs mount options got updated
- HiDPI support

**Bug-fixes:**

- The locales bug in calamares got fixed
- F2FS has been removed for the grub boot loader since it is currently not working (calamares issue), it can be still with systemd-boot used
- Calamares shows now the correct default filesystem
- Gnome ISO got fixed
- Missing packages at the live ISO has been added for the offline installation
- btrfs swap luksencryption got fixed
- usual translation fixes

22.06
-----

Following known bugs has been fixed:

- Install failed when a generic CPU was used
- KDE did automatically mount zfs paritions which resulted that the auto login into the ISO did not worked anymore

**Improvements:**

- The firewall from the server has been corrected, cloudflare did blocked users as "bots", which resulted then into a error at installing
- Added theming support for Gnome, XFCE, OpenBox
- Updated our wiki

**_CachyOS - Kernel - Manager_**
Also we are excited to announce our CachyOS-Kernel-Manager.
Their you have the possibility to install the kernel from the repo and also configure with a GUI your own kernel build which makes is very easy to customize it to his own suits.

Following options you can select for a kernel compile:

- Scheduler (BMQ, BORE, cacULE, cfs, PDS, TT)
- NUMA disabled or enabled
- KBUILD CFLAGS (-O3 or -O2)
- Set performance governor as default
- Enable BBR2
- Tickrate (500Hz, 600Hz, 750Hz, 1000Hz)
- tickless (idle, perodic, full)
- disable MQ-Deadline I/O Scheduler
- disable Kyber I/O Scheduler
- Enable or disable MG-LRU
- Enable or disable DAMON
- Enable or disable Speculative page fault
- Enable or disable LRNG (Linux Random Number Generator)
- Apply Kernel automatic Optimization (Does automatically detect your CPU March)
- Apply Kernel Optimization slecting (You will see a list of different CPU-Marches and can select with a number yours)
- Disable debug (it lowers the size of the kernel)
- Enable or disable nf cone
- Enable LTO (Full, Thin, No)

22.05
-----

CachyOS was founded a year ago. After almost one year of development, we are really proud to announce our first Stable Release of GUI Installer.
We spent a lot of time investigating repo management, kernel development, infrastructure, theming, ... and finally put them all into the CachyOS GUI Installer.
All the features we worked on and implemented into the Installer are just trying to offer users a completely customizable experience.

The most exciting changes are that we use now for the online install pacstrap which provide then a complete clear installed environment and we do support a complete native support for the zfs filesystem

Since Discord restrict the length of the messages the full announcement can be found here:

<https://discuss.cachyos.org/t/cachyos-gui-installer-changelog/>

Download can be found here:
<https://mirror.cachyos.org/ISO/kde/220522/>
<https://sourceforge.net/projects/cachyos-arch/>

<a id="configuration-automount-with-fstab"></a>
#### Automount Additional Drives Through fstab at Boot

This tutorial describes the basics of utilizing the fstab file located in /etc/ in order to mount static drives during boot. It briefly explains how to find a partition or drive's UUID, what some options do, and further reading should the information provided be insufficient.

<a id="configuration-automount-with-fstab-prerequisites"></a>
### Prerequisites

- Root or sudo access

<a id="configuration-automount-with-fstab-adding-entries-to-etcfstab"></a>
### Adding Entries to /etc/fstab

> **Note – NTFS on Linux:**
> The NTFS filesystem can be unstable under Linux, whether using the ntfs3 or ntfs-3g driver. Use it at your own risk. For better stability and performance, consider Linux native filesystems like ext4, xfs, or btrfs.

<a id="configuration-automount-with-fstab-1-list-the-uuids-of-your-partitions"></a>
#### 1. List the UUIDs of your partitions

```sh title="Open a terminal and run the following command"
lsblk -f
```

```text title="Example output"
# NAME        FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
# zram0                                                                              [SWAP]
# nvme0n1
# ├─nvme0n1p1 vfat   FAT32       E04D-9F05
# ├─nvme0n1p2
# ├─nvme0n1p3 ntfs               08A24E90A24E81E4                      715.4G    50%
# ├─nvme0n1p4 vfat   FAT32       E09C-D4DA                             628.1M    39% /boot
# ├─nvme0n1p5 ext4   1.0         187a9f06-9411-48d9-b941-f03c2e605812  203.6G    47% /
# └─nvme0n1p6 ntfs
```

In our example, we know that we want to mount a Windows partition, which is ntfs. We also know that roughly half its space is available. Therefore, we can determine that the partition we want to mount is `nvme0n1p3` and its UUID to be `08A24E90A24E81E4`, with a file system of `ntfs` in this example.

<a id="configuration-automount-with-fstab-2-identifying-your-partition"></a>
#### 2. Identifying your partition

Often `lsblk -f` will provide all the information you need to mount your disk through /etc/fstab at this point. If you're still unsure which is the correct partition, you can run the following command:

```sh
sudo fdisk -l
```

```text title="Example output"
# Device              Start        End    Sectors  Size Type
# /dev/nvme0n1p1       2048     206847     204800  100M EFI System
# /dev/nvme0n1p2     206848     239615      32768   16M Microsoft reserved
# /dev/nvme0n1p3     239616 2997384182 2997144567  1.4T Microsoft basic data
# /dev/nvme0n1p4 2997385216 2999482367    2097152    1G EFI System
# /dev/nvme0n1p5 2999482368 3905454079  905971712  432G Linux root (x86-64)
# /dev/nvme0n1p6 3905454080 3907026943    1572864  768M Windows recovery environment
```

We already know our UUID in this example. However, `fdisk -l` can make it a bit more clear to us by showing the exact size of the partition (1.4T) as well as its type (Microsoft basic data).

That should make it abundantly clear to us that the partition we want is `nvme0n1p3` with a UUID of `08A24E90A24E81E4` as described earlier. We knew earlier, but now we just know it for sure.

Once you are confident you've found the correct partition, copy the UUID. Copying from the terminal emulator is typically done with `ctrl+shift+C`.

<a id="configuration-automount-with-fstab-3-adding-an-entry-to-etcfstab"></a>
#### 3. Adding an Entry to /etc/fstab

Now that we've obtained the UUID of our partition, it's time to open up the fstab file.

Feel free to use your text editor of choice. In this example, we will use nano. In order to edit the fstab file, it must be opened as root:

```sh
sudo nano /etc/fstab
```

Using the arrow keys, navigate to the bottom of the fstab file, then create our new entry on an empty new line:

```sh
UUID=08A24E90A24E81E4 /media/windows ntfs3 defaults,nofail,uid=1000,gid=1000,rw,user,exec,umask=000 0 0
```

The break down of this entry is as follows:

- `UUID=08A24E90A24E81E4` is the file system we want to mount, identified by its UUID. There are other methods to identify your filesystem, though UUID tends to be safest. Additional methods listed [here](https://wiki.archlinux.org/title/Fstab#Identifying_file_systems).

- `/media/windows` is the mount point of our drive. The [Linux Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) says that `/media/` is the proper location for removable drives to be mounted. `windows` indicates the directory we wish to mount our drive to. Each drive we want to mount will need its own directory.

- `ntfs3` is the filesystem type to be used. We are explicitly using the ntfs3 kernel driver in our example. Other examples would be `ext4`, `xfs` or similar. This explicit filesystem type declaration can be replaced with `auto` to allow the mount command to make its best guess.

- `defaults,nofail,uid=1000,gid=1000,rw,user,exec,umask=000`: These are mount options:

- `defaults`: a standard set of options including `rw, suid, dev, exec, auto, nouser, and async.`

- `nofail`: allows the boot process to continue even if this mount fails.

- `uid=1000` and `gid=1000`: sets the user and group ownership of the mounted files to the user and group with ID 1000.

- `rw`: mounts the filesystem as read-write.

- `user`: allows a non-root user to mount the filesystem.

- `exec`: allows execution of binaries on the mounted filesystem.

- `umask=000`: sets the file permission mask to allow read, write, and execute permissions for everyone.

- `the first 0` dump is typically deprecated in modern systems. Leaving this at 0 won't hurt anything. Feel free to read more about it [here](https://linux.die.net/man/8/dump).

- `the second 0` sets the order for file system checks at boot time. For a root partition, this should be 1 unless your root file system is btrfs, which should otherwise be set to 0. All other file systems in your fstab should be either 0 (disabled) or 2. More information [here](https://man.archlinux.org/man/fsck.8).

For a more in depth look of each option, visit these two [fstab man page](https://man7.org/linux/man-pages/man5/fstab.5.html) and [mount man page](https://man7.org/linux/man-pages/man8/mount.8.html)

<a id="configuration-automount-with-fstab-more-info"></a>
##### More info

As an aside, all options after the filesystem type declaration are optional if you do not change them from the default.

Thus

`UUID=&lt;partition UUID&gt; /media/foo somefs`

and

`UUID=&lt;partition UUID&gt; /media/foo somefs defaults 0 0`

are equivalent.  `somefs` followed by nothing is implicitly `somefs defaults 0 0`

<a id="configuration-automount-with-fstab-4-finishing-up"></a>
#### 4. Finishing Up

If you wish to mount the drive you created an entry for now, you need to run the following:

```sh
sudo systemctl daemon-reload
```

and then:

```sh
sudo mount -a
```

Your drive should now appear under `/media/windows` and will appear there each time you reboot.

```sh
ls /media/windows
# '$Recycle.Bin'             Linux                  SteamLibrary
# AMD                       Modding                swapfile.sys
# Apps                      pagefile.sys          'System Volume Information'
# bootTel.dat               PerfLogs               Users
# Development               ProgramData            WiiU
# 'Documents and Settings'  'Program Files'         Windows
# DumpStack.log.tmp        'Program Files (x86)'   XboxGames
# FanControl                Recovery               xiv_modding
# Games                     RetroArch-Win64
# Intel                    'Ship of Harkinian'
 ```

 If you wish to create a link to your newly mounted drive in your home directory, you can run the following:

 ```sh
 ln -s /media/windows ~/Windows
 ```

 To show it worked:

 ```sh
 ls ~/Windows
# '$Recycle.Bin'             Linux                  SteamLibrary
# AMD                       Modding                swapfile.sys
# Apps                      pagefile.sys          'System Volume Information'
# bootTel.dat               PerfLogs               Users
# Development               ProgramData            WiiU
#'Documents and Settings'  'Program Files'         Windows
# DumpStack.log.tmp        'Program Files (x86)'   XboxGames
# FanControl                Recovery               xiv_modding
# Games                     RetroArch-Win64
# Intel                    'Ship of Harkinian'
 ```

<a id="configuration-automount-with-fstab-tldr"></a>
### tl;dr

- Find the **UUID** of your partition

```sh
lsblk -f
```

- Open `/etc/fstab`

```sh
sudo nano /etc/fstab
```

- Create an entry in the bottom of the file

```sh
UUID=&lt;partition UUID&gt; /media/foo somefs defaults 0 0
```

Replacing `&lt;partition UUID&gt;`, `foo`, and `somefs` with your UUID, directory, and filesystem. eg., ext4, as well as setting any other options you may want after defaults, such as `_netdev` for a NAS, or `nofail` for any non-critical drive.

- Reload your daemon

```sh
sudo systemctl daemon-reload
```

- Mount your drive

```sh
sudo mount -a
```

This drive is now mounted, and will now be mounted on boot moving forward as well.

<a id="configuration-automount-with-fstab-additional-reading"></a>
### Additional reading

- [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
- [FHS on /media/](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s11.html)
- [Manual for dump](<https://linux.die.net/man/8/dump>)
- [Manual for fsck](https://man.archlinux.org/man/fsck.8)
- [Man page for fstab](https://man.archlinux.org/man/fstab.5.en)
- [Arch Linux Wiki entry for fstab](https://wiki.archlinux.org/title/Fstab)

<a id="configuration-boot-manager-configuration"></a>
#### Boot Manager Configuration

<a id="configuration-boot-manager-configuration-systemd-boot"></a>
### systemd-boot

systemd-boot has two kinds of configuration files: one for systemd-boot itself in `/boot/loader/loader.conf`, and one for each
individual kernel entry in `/boot/loader/entry`.

<a id="configuration-boot-manager-configuration-loader-configuration"></a>
#### Loader configuration

In this configuration file, you can change the default entry and timeout of systemd-boot

```shell
# /boot/loader/loader.conf

default @saved
timeout 5
#console-mode keep # This option configures the resolution of the console.
```

<a id="configuration-boot-manager-configuration-kernel-commandline-configuration"></a>
#### Kernel Commandline Configuration

We provide a tool for easier configuration of systemd-boot: [`sdboot-manage`](https://github.com/CachyOS/CachyOS-PKGBUILDS/tree/master/systemd-boot-manager).
One of the perks of this tool is global kernel commandline configuration. The configuration file for `sdboot-manage` is located in `/etc/sdboot-manage.conf`.

Edit the `LINUX_OPTIONS=` line in `/etc/sdboot-manage.conf` to change kernel parameters.

```shell
# /etc/sdboot-manage.conf
LINUX_OPTIONS="zswap.enabled=0 nowatchdog quiet splash"
```

After making changes, regenerate all systemd-boot entries with the following command

```shell
sudo sdboot-manage gen
```

<a id="configuration-boot-manager-configuration-refind"></a>
### rEFInd

Like [systemd-boot](#configuration-boot-manager-configuration-systemd-boot), rEFInd has two configuration files. `refind.conf` located in
`boot/efi/EFI/refind` is mainly for changing how rEFind behaves, while `/boot/refind_linux.conf` is for managing your boot options.
`refind.conf` contains extensive comments explaining all its options.

<a id="configuration-boot-manager-configuration-kernel-commandline-configuration"></a>
#### Kernel Commandline Configuration

To pass kernel parameters to the commandline, modify "Boot using default options" in `/boot/refind_linux.conf`

```shell
# /boot/refind_linux.conf

"Boot using default options"     "root=PARTUUID=1cb353ec-7f03-4820-8b4b-03baf53a208f rw zswap.enabled=0 nowatchdog quiet splash"
```

Changes to both configuration files will immediately take effect. Running a command to "save" changes is unnecessary.

<a id="configuration-boot-manager-configuration-grub"></a>
### GRUB

Unlike [systemd-boot](#configuration-boot-manager-configuration-systemd-boot) and [rEFInd](#configuration-boot-manager-configuration-refind),
GRUB only has one configuration file located in `/etc/default/grub`. There is pretty good documentation in this file that explains what
each option does.

<a id="configuration-boot-manager-configuration-hiding-the-grub-boot-menu"></a>
#### Hiding the GRUB Boot Menu

To hide the GRUB menu, simply set these following options accordingly.

```shell
# /etc/default/grub

GRUB_TIMEOUT='0'
GRUB_TIMEOUT_STYLE=hidden
```

Press ESC to get access to the GRUB prompt. From here run `normal` or `exit` to get back to the familiar GRUB boot menu.

<a id="configuration-boot-manager-configuration-kernel-commandline-configuration"></a>
#### Kernel Commandline Configuration

To pass kernel parameters to the commandline with GRUB, we need to edit `GRUB_CMDLINE_LINUX_DEFAULT` within `/etc/default/grub`.

```shell
# /etc/default/grub

GRUB_CMDLINE_LINUX_DEFAULT='nowatchdog zswap.enabled=0 quiet splash'
```

Every time we modify the GRUB configuration file, we need to remake the config with the following command:

```shell
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

<a id="configuration-boot-manager-configuration-bootable-btrfs-snapshots"></a>
#### Bootable BTRFS snapshots

> **Note:**
> If your CachyOS installation is from before the August release, you might need to enable the bootable BTRFS snapshots feature manually.
>
> Otherwise, you can skip this section, as it has been enabled by default since the August release.

To enable the feature, install the grub-btrfs-support package:

```sh
sudo pacman -S grub-btrfs-support
```

This package installs the necessary scripts and hooks to automatically detect BTRFS snapshots and add them to the GRUB menu.

Once installed, your snapshots will appear in the GRUB menu, similar to Limine's behavior.

<a id="configuration-boot-manager-configuration-limine"></a>
### Limine

Limine is a modern bootloader known for its simple configuration. This guide covers the basics to get you started.

Configuration primarily happens in `/boot/limine.conf` (or sometimes in the EFI system partition) for menu settings, and `/etc/default/limine` for kernel parameters.

<a id="configuration-boot-manager-configuration-boot-menu-configuration"></a>
#### Boot Menu Configuration

This file controls the boot menu's behavior and appearance. Changes made here take effect immediately after saving – no extra commands are needed.

* **Timeout:** Sets how many seconds Limine waits before automatically booting the default entry.

  ```shell
  # /boot/limine.conf

  timeout: 5
  ```

* **Default Entry:** Specifies which menu entry boots by default. Entries are numbered starting from 1. If not set, the default value is 1.

  ```shell
  # /boot/limine.conf

  default_entry: 2 # Boot the second entry by default
  ```

> **Tip:**
> If `default_entry` points to a directory (e.g., `/+CachyOS`), autoboot will be disabled. To autoboot an entry within a directory, `default_entry` must point directly to that specific entry number.

Example (`/boot/limine.conf`):

```shell
# /boot/limine.conf

timeout: 5
default_entry: 2 # Points directly to the 'linux-cachyos' entry below

/+CachyOS        # Entry 1: A directory (use /+ to expand by default)
//linux-cachyos  # Entry 2: The actual bootable entry
    protocol: linux
    kernel_path: boot():/vmlinuz-linux-cachyos
    cmdline: quiet splash root=UUID=... rw # Basic kernel parameters
    module_path: boot():/initramfs-linux-cachyos.img
```

> **Note:**
> `boot():/` refers to the root of the boot drive.

<a id="configuration-boot-manager-configuration-theming"></a>
#### Theming

You can customize the visual appearance of the Limine boot menu:

* **Wallpaper:** Set a background image. Supported formats include BMP, PNG, and JPEG.

  ```shell
  # /boot/limine.conf

  wallpaper: boot():/splash.png
  wallpaper_style: stretched # Options: 'stretched', 'tiled', 'centered'
  backdrop: 000000           # Background color (RRGGBB hex) if style is 'centered'
  ```

* **Fonts:** Use a [custom font file](https://github.com/viler-int10h/vga-text-mode-fonts) and adjust its size.

  ```shell
  # /boot/limine.conf

  term_font: boot():/custom_font.F16
  term_font_scale: 2x2 # Scales font size, useful for high-resolution displays
  ```

* **Colors:** Modify terminal text and background colors.

  ```shell
  # /boot/limine.conf

  term_background: 80000000 # Example: Semi-transparent black (AARRGGBB)
  # Other color options like term_foreground, etc., are available.
  ```

<a id="configuration-boot-manager-configuration-kernel-command-configuration"></a>
#### Kernel Command Configuration

On CachyOS, kernel entries in the Limine boot menu are **automatically managed**. When you install or remove kernels, the `limine-mkinitcpio-hook` uses the `limine-entry-tool` utility in the background to update the boot entries.

While entries are handled automatically, you can **configure the kernel parameters** (also known as the kernel command line) that are passed to the kernel when it boots.

1. **Edit the configuration file:** Modify the `KERNEL_CMDLINE` variables in `/etc/default/limine`. You can set default parameters for all kernels or specific parameters for certain kernel names (e.g., `linux-cachyos`).

   ```shell
   # /etc/default/limine

   # Default parameters for most kernels
   KERNEL_CMDLINE[default]="quiet splash rd.udev.log_priority=3"

   # Specific parameters for the 'linux-cachyos' kernel
   KERNEL_CMDLINE["linux-cachyos"]="quiet splash mitigations=off"

   # Parameters for fallback entries (if generated)
   # KERNEL_CMDLINE[fallback]="..."
   ```

2. **Apply the changes:** After saving `/etc/default/limine`, you need to regenerate your initramfs images and update the Limine entries to apply the new kernel parameters. Run the following command:

   ```bash
   sudo limine-mkinitcpio
   ```

   This command triggers the `mkinitcpio` process, which includes the `limine-mkinitcpio-hook`, ensuring your changes in `/etc/default/limine` are incorporated into the boot entries at `/boot/limine.conf`.

<a id="configuration-boot-manager-configuration-learn-more"></a>
### Learn more

* [loader.conf manual page](https://man.archlinux.org/man/loader.conf.5)
* [rEFInd: Configuring the boot manager](https://www.rodsbooks.com/refind/configfile.html)
* [GRUB Manual: Configuration](https://www.gnu.org/software/grub/manual/grub/grub.html#Configuration)
* [Official Limine Configuration Docs](https://github.com/limine-bootloader/limine/blob/v9.x/CONFIG.md)
* [limine-entry-tool Project](https://gitlab.com/Zesko/limine-entry-tool)

<a id="configuration-enabling-hardware-acceleration-in-google-chrome"></a>
#### Chromium-Based Browsers HW Acceleration

This guide outlines enabling hardware acceleration in Chromium-based browsers on CachyOS. This offloads video/graphics tasks to your GPU, improving performance.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-prerequisites"></a>
### Prerequisites

**Required:**
* **Chromium-based Browser:** (e.g., Chrome, Brave, Ungoogled Chromium, Edge)
* **GPU Drivers/APIs:** Up-to-date Mesa (AMD/Intel) or NVIDIA drivers, with Vulkan/VA-API/VDPAU configured.

**Optional:**

* **amdgpu_top:** Install `amdgpu_top` from the repository through package manager if you wish to monitor AMD GPU activity from the terminal.
* **nvtop:** (Intel GPU's only) Install `nvtop` (Lunar Lake) and `intel-gpu-tools` (Pre-Lunar Lake) through the octopi package manager if you wish to monitor Intel GPU activity from the terminal.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-contribution"></a>
### Contribution

This guide is extensible. If you have a working hardware acceleration setup for a specific GPU and Chromium-based browser, contribute by adding a new section under "GPU & Browser Configurations." Include:

* **Browser Name**
* **GPU Model**
* **Flags:** `~/.config/[browser]-flags.conf` content.
* **File Path:** Full path to the flags file.
* **Notes (Optional):** Key drivers, packages, or setup specifics.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-setup-steps"></a>
### Setup Steps

1. Identify Flags File: Locate your browser's flags file path in "GPU & Browser Configurations."
2. Edit Flags File: Open/create the file using `nano` (or your preferred text editor like `micro`, `vim`).

    ```bash
    nano [PATH_TO_YOUR_BROWSER_FLAGS_FILE]
    # Example: nano ~/.config/chrome-flags.conf
    ```

3. Add Flags: Paste the relevant GPU/browser flags into the file.
4. Save & Close.
5. Restart Browser: Close all browser instances and relaunch.
6. Verify: Navigate to `chrome://gpu` (or `brave://gpu`, `edge://gpu`, etc.). Confirm "Hardware accelerated" status under "Video Acceleration Information" and "Graphics Feature Status."

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-how-to-verify-video-hardware-acceleration"></a>
### How to Verify Video Hardware Acceleration

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-amd-gpus-amdgputop"></a>
###### AMD GPUs (amdgpu_top)

1. Open a terminal and run the command:
    ```bash
    amdgpu_top
    ```
2. Start playing a video in your browser (e.g., on YouTube).
3. Observe the `media` section in `amdgpu_top`. You should see some utilization here, indicating your GPU's media engine is active. If it remains at 0% during video playback, hardware acceleration might not be fully engaged for decoding.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-intel-gpus-nvtop"></a>
###### Intel GPUs (nvtop)

1. Open a terminal and run the command:
    ```bash
    sudo nvtop
    ```
2. Start playing a video in your browser (e.g., on YouTube).
3. Observe the `ENC/DEC` percentage in `nvtop`, the percentage should increase if video decoding is working in hardware.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-intel-gpus-intelgputools"></a>
###### Intel GPUs (intel_gpu_tools)

1. Open a terminal and run the command:

    ```bash
    sudo intel_gpu_top
    ```

Note: Some newer Intel gpu's such as Lunar Lake GPU's no longer expose the gpu performance counters with `intel_gpu_top`, use `nvtop` for these systems

2. Start playing a video in your browser (e.g., on YouTube).
3. Observe the `Video` and `VideoEnhance` percentage in intel_gpu_top, the percentage should increase if video decoding is working in hardware.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-browser-developer-tools"></a>
###### Browser Developer Tools

1. Open your Chromium-based browser.

2. Start playing a video (e.g., on YouTube or a local file).

3. Open Developer Tools: Press `F12` or `Ctrl+Shift+I`.

4. Navigate to the **Media** tab. If you don't see it, click the three dots (`...`) or `>>` (More tabs) on the Developer Tools toolbar, then select `Media`.

5. In the "Players" section on the left, click on the entry corresponding to your video.

6. In the main panel, scroll down to the **Video Decoder** section.

7. Look for the `Hardware decoder` label. It should be `true`. If it says `false` or shows a software decoder name (e.g., `FFmpegVideoDecoder`, `VpxVideoDecoder`, `Dav1dVideoDecoder`), hardware acceleration is not active for that video.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-gpu-browser-configurations"></a>
### GPU & Browser Configurations

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-amd-radeon-rx-6900-xt-google-chrome"></a>
#### AMD Radeon RX 6900 XT (Google Chrome)

* **Browser:** Google Chrome

* **GPU:** AMD Radeon RX 6900 XT

* **Flags File:** `~/.config/chrome-flags.conf`

```bash
--use-gl=angle
--use-angle=vulkan
--enable-features=Vulkan,VulkanFromANGLE,DefaultANGLEVulkan,AcceleratedVideoDecodeLinuxZeroCopyGL,AcceleratedVideoEncoder,VaapiIgnoreDriverChecks,UseMultiPlaneFormatForHardwareVideo
--ozone-platform-hint=x11
```

**Notes:** Leverages Vulkan (via ANGLE) and VA-API. `--ozone-platform-hint=x11` can be useful even on Wayland for certain acceleration paths.

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-nvidia-rtx-4090-vivaldi"></a>
#### Nvidia RTX 4090 (Vivaldi)

* **Browser:** Vivaldi

* **GPU:** Nvidia RTX 4090

* **Flags File:** `~/.config/vivaldi-stable.conf`

```bash
--enable-features=VaapiVideoDecoder,AcceleratedVideoDecodeLinuxGL,AcceleratedVideoDecodeLinuxZeroCopyGL
```

* **Flags File:** `/usr/share/applications/vivaldi-stable.desktop`

```bash
# Keep all other lines the same
# You should only change this Exec= entry under the '[Desktop Entry]' section
Exec=/usr/bin/vivaldi-stable --enable-features=VaapiVideoDecoder,AcceleratedVideoDecodeLinuxGL,AcceleratedVideoDecodeLinuxZeroCopyGL %U
```

**Notes:**

You should only need to aply one of these conf file changes, but doing so on both should not cause issues.

Alternatively you can do the following for KDE:
1. Delete any Task Manager / taskbar shortcuts for Vivaldi
2. Search for `Vivaldi` in the Application Launcher list
3. Right-click the entry in the Application Launcher and select `Edit Application...`
4. In the `Command-line arguments` section, add in the following arguments before the last argument `%U`:
```
--enable-features=VaapiVideoDecoder,AcceleratedVideoDecodeLinuxGL,AcceleratedVideoDecodeLinuxZeroCopyGL
```
5. Launch Vivaldi and pin the process to your Task Manager / taskbar

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-amd-radeon-rx-550-ungoogled-chromium"></a>
#### AMD Radeon RX 550 (UnGoogled Chromium)

* **Browser:** UnGoogled Chromium

* **GPU:** AMD Radeon RX 550

* **Flags File:** `~/.config/chromium-flags.conf`

```bash
--enable-wayland-ime
--ozone-platform=wayland
--enable-features=AcceleratedVideoDecodeLinuxGL,AcceleratedVideoDecodeLinuxZeroCopyGL,AcceleratedVideoEncoder,WaylandSessionManagement,WaylandTextInputV3,WaylandUiScale,WaylandWindowDecorations
```

**Notes:**

If you're using X11, use this:
```bash
--ozone-platform=x11
--enable-features=AcceleratedVideoDecodeLinuxGL,AcceleratedVideoDecodeLinuxZeroCopyGL,AcceleratedVideoEncoder
```

---

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-template-to-contribute"></a>
#### Template to contribute

<a id="configuration-enabling-hardware-acceleration-in-google-chrome-your-browser-your-gpu-model-contributed-by-your-namehandle"></a>
#### [Your Browser] - [Your GPU Model] (Contributed by [Your Name/Handle])

* **Browser:** [e.g., Brave, Ungoogled Chromium, Microsoft Edge, Vivaldi, Opera, Chromium]

* **GPU:** [e.g., NVIDIA GeForce RTX 3080, Intel Iris Xe]

* **Flags File Path:** (Crucial, varies per browser!)

* Common `.conf` paths:

* Chromium: `~/.config/chromium-flags.conf`

* Brave Browser: `~/.config/brave-flags.conf`

* Ungoogled Chromium: `~/.config/ungoogled-chromium-flags.conf`

* `.desktop` file modification: Some browsers (Brave, Edge, Vivaldi, Opera) might require editing the `Exec=` line in their `.desktop` file (copy from `/usr/share/applications/` to `~/.local/share/applications/` first).

Flags Content (for `.conf` file or `Exec=` line):

```bash
# Paste your flags here.
# For .desktop files, flags are space-separated after the executable.
```

**Notes (Optional):**

* Required drivers (e.g., `nvidia-dkms`, `intel-media-driver`).

* Specific setup considerations or `.desktop` file modification instructions.

<a id="configuration-dual-gpu"></a>
#### Dual GPU Setup Guide

<a id="configuration-dual-gpu-whats-hybrid-graphics"></a>
### What's hybrid graphics?

Hybrid graphics is a hardware configuration in which you have two graphics
cards that can work in tandem with each other. This approach is mainly found in
laptops where you have integrated graphics (iGPU) of your CPU, and discrete
graphics (dGPU).

The main advantage is that integrated graphics should (but not necessarily) only be
used for low-profile tasks, such as surfing the Internet, watching videos, etc.
On the other hand, discrete graphics are used for high-performance
things like gaming, video editing, 3D modeling, and so on.

Consequently, if two GPUs share "big" and "small" tasks, then if we have only
"small" tasks running at the moment, we don't need to use our dGPU, so it can
simply be disabled (as if asleep), thereby significantly reducing power consumption.
This way when our dGPU is needed again (we run an application using it),
it will wake up and start working.

<a id="configuration-dual-gpu-whats-prime-offload"></a>
### What's PRIME Offload?

PRIME is a unifying technology for working with different sets of hybrid
graphics in Linux, like NVIDIA Optimus/AMD Dynamic Switchable Graphics. PRIME
Offload is an implementation of the idea of moving the execution of render from
one GPU to another in Linux.

PRIME support in a closed NVIDIA driver actually started only with the 435.17 driver.
So if you are a user of the outdated 390xx or even 340xx driver branches,
PRIME Offload will not work for you. Note that we also
strongly discourage you from using outdated ways to handle hybrid graphics,
such as nvidia-xrun or Bumblebee. They are obsolete and unsupported (Bumblebee
has not been updated for over 8 years), run solely on hacks and have low
performance. At the same time the Nouveau driver supports PRIME Offload, which
can be an alternative for older dGPUs.

In CachyOS, **you don't need to configure anything to make PRIME Offload work**.
With the nvidia-utils package and cachyos-settings you already have everything
you need to use PRIME Offload.

Also, please avoid using tools like optimus-manager. They may seem quite handy
to you, but believe us, they can cause a lot of issues and you really don't
need them if your dGPU supports PRIME Offload and dynamic power management.

<a id="configuration-dual-gpu-how-to-use-prime-offload"></a>
#### How to use PRIME Offload

To indicate PRIME that you want to use discrete graphics instead of integrated
graphics, you must specify a number of environment variables before running the
program:

```bash
__NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia &lt;program&gt;
```

This set of variables looks very cumbersome and easy to forget, so you can
install the `nvidia-prime` package (`sudo pacman -S nvidia-prime`), which
contains script-alias for all these variables. Then running an application
using it will look like this:

```bash
prime-run &lt;program&gt;
```

Where `&lt;program&gt;` is the name of command that runs your application.

> **Note:**
> Some DX12 games have trouble choosing the dGPU even with `prime-run`
> To workaround this, add the env var `VK_DRIVER_FILES=/usr/share/vulkan/icd.d/nvidia_icd.json`
> before `prime-run` wrapper script.

For configurations where both graphics cards are managed by open Mesa drivers
(e.g. AMD+AMD, AMD+Intel or even Intel+NVIDIA where NVIDIA discrete graphics
are managed by open source Nouveau driver), nothing needs to be configured and
to use discrete graphics you only need to specify the `DRI_PRIME=1`
environment variable before launching applications or games, similar to all
those variables described earlier for NVIDIA or use ready-made graphics methods
discussed below.

<a id="configuration-dual-gpu-graphical-method"></a>
### Graphical method

You might find launching all needed applications through the terminal using `prime-run` inconvenient.
Fortunately, some applications and desktop environments provide tools to control which GPU is used for specific applications.

<a id="configuration-dual-gpu-lutris"></a>
#### Lutris

To configure games to run with discrete graphics in Lutris you need to go to
settings (three strips in the bottom right corner of the window and
"Preferences" button). Next, go to *"Global Options"* -> *"Display"*. Here, you can select the GPU the game will run on.

![Image](src/assets/images/lutris-prime.png)

<a id="configuration-dual-gpu-steam"></a>
#### Steam

Steam doesn't have a specific setting to force a game to use discrete graphics. However, you can access the game's properties by clicking the gear icon before launching it. In the "Launch options" field, you can add the prime-run command or environment variables.
Example:

```bash
prime-run %command%
```

Be sure to add `%command%` after `prime-run`. Remember that game options come after the placeholder,
while system environment variables or commands should precede it.

![Image](src/assets/images/steam-prime.png)

<a id="configuration-dual-gpu-kde-plasma"></a>
#### KDE Plasma

Plasma has a very handy way to set up the startup of applications with discrete
graphics. However, this method only works if the switcheroo-control package and its corresponding service are installed on your system.

In a fresh installation of CachyOS, this package and service should already be
enabled by default via chwd.

```bash
sudo pacman -S switcheroo-control
sudo systemctl enable --now switcheroo-control
```

After having executed both commands, right click on the desktop entry you want on your desktop or in the
application menu then go to *"Properties"* -> *"Application"* -> *"Advanced Options"*.

You should have *"Run using dedicated graphics card"* checkbox checked.

![Image](src/assets/images/plasma-prime.jpg)

> **Note:**
> Using switcheroo-control allows these checkboxes to work on all PRIME
> configurations that don't even have NVIDIA dGPU, such as AMD-APU+AMD-Dedicated.

<a id="configuration-dual-gpu-gnome"></a>
#### GNOME

On GNOME, you should also install switcheroo-control as shown above and
right-click on the application icon and select *"Run using discrete graphics"*.
But note that GNOME does not remember this choice for later, and the next time you
run the application from the icon, its going to run using integrated graphics instead of discrete.

<a id="configuration-dual-gpu-cinnamon"></a>
#### Cinnamon

Similar to Plasma, Cinnamon also allows you to select the GPU for specific applications. Right-click the application's desktop entry, go to Properties, and enable the relevant option.

![Image](src/assets/images/cinnamon-prime.png)

If it's not available, make sure you have `switcheroo-control` installed and
its service enabled, because all desktop environments rely on it for this
functionality.

<a id="configuration-dual-gpu-troubleshooting"></a>
### Troubleshooting

<a id="configuration-dual-gpu-my-external-monitor-is-very-laggy-on-prime"></a>
#### "My external monitor is very laggy on PRIME"

This is a known NVIDIA driver issue. You should have the latest NVIDIA
driver installed and use Wayland with a compositor that supports explicit sync.
For GNOME this has been fixed in version 46.2. For Plasma 6 it will probably be
fixed with 6.1 although some users report normal performance already on 6.0.
Other environments/window managers still have this issue, so you need to switch
to the latest version of GNOME or Plasma to fix it.

<a id="configuration-gaming"></a>
#### Gaming with CachyOS Guide

Welcome to the guide for Gaming in CachyOS. We'll guide you through the essentials aspects on how to setup everything and have a great experience.

<a id="configuration-gaming-prerequisites"></a>
### Prerequisites

> **Caution:**
> Before we dive into the fun stuff, it’s essential to ensure that your graphics card drivers are installed and functioning correctly. If your graphics card isn’t performing optimally, you may encounter issues when playing games.

<a id="configuration-gaming-essential-packages"></a>
#### Essential Packages

To make things easier for you, CachyOS has grouped all the necessary packages for gaming into one meta package that includes all the necessary dependencies and libraries for gaming in Linux and a separate package for the tools and launchers/stores. This makes the installation and setup process for gaming faster and less convoluted for everyone.

*If you find that any packages are missing, feel free to let the CachyOS team know.*

Follow the steps below to start with the gaming setup.

<a id="configuration-gaming-meta-package"></a>
###### Meta Package

        ```sh
        sudo pacman -S cachyos-gaming-meta
        ```

<a id="configuration-gaming-tools-stores"></a>
###### Tools & Stores

    *This package includes the following:*
- Gamescope, Goverlay, Heroic Games Launcher, Lutris, MangoHud and Steam.
        ```sh
        sudo pacman -S cachyos-gaming-applications
        ```

<a id="configuration-gaming-cachyos-hello"></a>
###### CachyOS Hello

- Go to **Apps/Tweaks** and click on `Install Gaming packages`

*CachyOS Hello installs both packages `cachyos-gaming-meta` and `cachyos-gaming-applications`*

<a id="configuration-gaming-proton-cachyos"></a>
### Proton-CachyOS

Proton-CachyOS is based on Proton's `bleeding-edge` branch and applies a number of modifications on top of it.
- **Wine-staging patches**
- **Wine Fullscreen FSR**
- **Includes video and audio codecs for game cutscenes**
- **Support for umu-launcher including UMU-Protonfixes**
- **Adds early hotfixes/workarounds for games**

> **Note:**
> The `proton-cachyos` package from the CachyOS repositories is compiled against native system libraries, it doesn't use the Steam Linux Runtime. The target architecture depends on the repository. Currently `x86_64_v3`, `x86_64_v4` and `znver4` repositories use the same `x86_64_v3` binaries.

<a id="configuration-gaming-how-to-properly-set-multiple-launch-options"></a>
#### How to properly set multiple launch options
The launch options in Steam are constructed using the following pattern
- `&lt;env variables&gt; &lt;wrappers&gt; %command% &lt;application arguments&gt;`
- `&lt;env variables&gt;`: These are options in the form of `VARIABLE=value`. For example `PROTON_DXVK_D3D8=1` or `DXVK_HUD="fps,memory,version,api"`
- `&lt;wrappers&gt;`: Applications and scripts that modify how the real application is run. Arguments to the wrapper usually go after the wrapper's executable. For example `mangohud --dlsym` or `gamescope -W 1680 -H 1050 -w 1280 -h 720 -S fit -F fsr --mangoapp --`
- `%command%`: This is the real application. This should be specified exactly as is and Steam will replace it with the proper command when the application is run.
- `&lt;application arguments&gt;`: These are various arguments to the real application, and they depend on the application. For example `-dx11` should go here if the application supports it.

- Example: `__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1 prime-run game-performance %command% -dx11`

> **Caution:**
> Don't add multiple `%command%` by using them as separators for multiple launch options.
>
> Example: `__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1 %command% game-performance %command% prime-run %command%`
> - In this case, everything after the first `%command%` is going to be ignored because it's being treated as game arguments, therefore only `__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1` gets recognized as a launch option.

<a id="configuration-gaming-environment-variables"></a>
##### Environment Variables

<a id="configuration-gaming-graphics-upscaling"></a>
###### Graphics & Upscaling

- DLSS & NVIDIA Features
- `PROTON_DLSS_UPGRADE=1`: Automatically upgrades DLSS to the latest version
- `PROTON_DLSS_INDICATOR=1`: Shows DLSS status indicator in-game
- `PROTON_NVIDIA_LIBS=1`: Enables NVIDIA libraries (PhysX, CUDA) - not needed for DLSS/ray tracing

**Advanced NVIDIA Controls:**

- `PROTON_NVIDIA_NVCUDA=1`: Enables CUDA support only
- `PROTON_NVIDIA_NVENC=1`: Enables NVENC encoding only
- `PROTON_NVIDIA_NVML=1`: Enables NVML monitoring
- `PROTON_NVIDIA_NVOPTIX=1`: Enables OptiX ray tracing
- `PROTON_NVIDIA_LIBS_NO_32BIT=1`: Only enable in 64-bit games (fixes RTX 4000+ performance issues)

- AMD & Intel Upscaling
- `PROTON_FSR4_UPGRADE=1`: Automatically upgrades FSR to latest AMD version
- `PROTON_FSR4_RDNA3_UPGRADE=1`: Uses RDNA3-optimized FSR4 DLL
- `PROTON_XESS_UPGRADE=1`: Automatically upgrades XeSS to latest version

<a id="configuration-gaming-display-hdr"></a>
###### Display & HDR

- Wayland & Display
- `PROTON_ENABLE_WAYLAND=1`: Enables native Wayland support
- **Benefits**: HDR without Gamescope, improved latency/frame pacing
- **Caveats**: Breaks Steam Overlay, currently experimental
- `PROTON_NO_WM_DECORATION=1`: Disables window manager decorations
- **Fixes**: Borderless fullscreen issues, mouse clicking through windows

- HDR Support
- `PROTON_ENABLE_HDR=1`: Enables HDR output support
- **Requirements**: Gamescope with `--hdr-enabled` OR `PROTON_ENABLE_WAYLAND=1`
- **Setup**: [Additional configuration needed](https://wiki.archlinux.org/title/HDR_monitor_support)

<a id="configuration-gaming-performance-caching"></a>
###### Performance & Caching

- CPU & Sync Performance
- `PROTON_USE_NTSYNC=1`: Uses NTSync for better CPU performance
- **Best for**: CPU-bound games, replaces WINESync
- **Note**: Experimental, may cause issues in some games
- **Verification**: Use `lsof /dev/ntsync` (MangoHud reports incorrectly)

- Shader & Cache Management
- `PROTON_LOCAL_SHADER_CACHE=0`: Disables per-game shader cache
- `PROTON_ENABLE_MEDIACONV=1`: Enables Proton Media Converter
- **Note**: Testing purposes only

- AMD Anti-Lag
- `ENABLE_LAYER_MESA_ANTI_LAG=1`: Enables AMD Anti-Lag for reduced input latency
> **Danger:**
> proton-cachyos disables this because it prevents FSR4 upgrades and can trigger stuttering or other issues ([details](https://github.com/CachyOS/CachyOS-PKGBUILDS/pull/909)).

<a id="configuration-gaming-input-compatibility"></a>
###### Input & Compatibility

- Controller & Input
- `PROTON_PREFER_SDL=1`: Workaround for controller detection issues
- `PROTON_NO_STEAMINPUT=1`: Disables Steam Input support
- **Fixes**: Wayland controller/gamepad issues

<a id="configuration-gaming-setting-up-proton-cachyos-with-lutris-and-heroic"></a>
#### Setting Up Proton-CachyOS with Lutris and Heroic

> **Note – The following configuration only applies to proton-cachyos. If you're using proton-cachyos-slr, -GE or -EM, you can skip this section.:**
> Make sure you have umu-launcher from CachyOS installed in your system.
> ```sh title='Install it with the following command:'
> sudo pacman -S cachyos/umu-launcher
> ```

<a id="configuration-gaming-lutris-global"></a>
###### Lutris Global

1. In the main Lutris screen, click the cogwheel icon next to Wine.
2. Go to the **Runner Options** tab and confirm that your settings match the following:
- **Wine version** = `proton-cachyos`
- **Use System winetricks** = *Disabled*
- **Graphics**
- **Enable DXVK** = `Enabled`
- Note: User-defined versions of **DXVK**, **VKD3D** and **DXVK-NVAPI** are not applied when using `umu-launcher`
3. Navigate to the **System Options** tab.
- **Lutris**
- **Disable Lutris Runtime** = `Enabled`
- **Prefer system libraries** = `Enabled`
4. Continue scrolling down to the **Game execution** section and locate the **Environment variables** table
5. Add the following environment variables:
- **Key**: `UMU_RUNTIME_UPDATE` *optional*
- **Value**: `0`
- *This will skip Steam Linux Runtime updates for proton-cachyos. Do not use this with any Proton that utilizes the Steam Linux Runtime, such as proton-cachyos-slr, -GE, or -EM.*
- **Key**: `PROTON_VERB` *optional*
- **Value**: `waitforexitandrun`
- *This allows protonfixes to work with a corresponding GAMEID.*
6. Click **Save** to apply the changes.

<a id="configuration-gaming-lutris-per-game"></a>
###### Lutris Per Game

1. Right Click in the game you want to configure, then click on **Configure**
2. Go to the **Runner Options** tab and confirm that your settings match the following:
- **Wine version** = `proton-cachyos`
- **Use System winetricks** = *Disabled*
- **Graphics**
- **Enable DXVK** = `Enabled`
- Note: User-defined versions of **DXVK**, **VKD3D** and **DXVK-NVAPI** are not applied when using `umu-launcher`
3. Navigate to the **System Options** tab.
- **Lutris**
- **Disable Lutris Runtime** = `Enabled`
- **Prefer system libraries** = `Enabled`
4. Continue scrolling down to the **Game execution** section and locate the **Environment variables** table
5. Add the following environment variables:
- **Key**: `UMU_RUNTIME_UPDATE` *optional*
- **Value**: `0`
- *This will skip Steam Linux Runtime updates for proton-cachyos. Do not use this with any Proton that utilizes the Steam Linux Runtime, such as proton-cachyos-slr, -GE, or -EM.*
- **Key**: `PROTON_VERB` *optional*
- **Value**: `waitforexitandrun`
- *This allows protonfixes to work with a corresponding GAMEID.*
6. Click **Save** to apply the changes.

<a id="configuration-gaming-heroic-games-launcher"></a>
###### Heroic Games Launcher

    
        1. Click on the `Configure` button next to the `Play Now` button in the game you want to run.
        2. In the `WINE` tab. Set the Wine Version to `Proton - proton-cachyos`.
    

<a id="configuration-gaming-anti-cheat-support"></a>
#### Anti Cheat Support

> **Caution – Important:**
> If you encounter issues with games using **Easy Anti-Cheat** (EAC) or **BattlEye** (BE) such as refusing to log in game servers, you can use the version of [Proton-CachyOS built using Steam Linux Runtime.](https://github.com/CachyOS/proton-cachyos/releases) **Also known as proton-cachyos-slr**

<a id="configuration-gaming-how-to-install-proton-cachyos-slr"></a>
#### How to install proton-cachyos-slr

<a id="configuration-gaming-protonup"></a>
###### protonup

1. Open a terminal and install `protonup`
    ```sh
    sudo pacman -S protonup-qt
    ```
2. Open **protonup-qt** and follow the screenshot:
![Image](src/assets/images/steam-protonup.png)
> **Note:**
> Choose the `x86-64_v3` version if your CPU supports **[AVX2](#installation-installation-prepare-x8664-microarchitecture-level-support)**.
>
> Otherwise download the one ending with `x86-64`.
3. Restart Steam if you had it opened.

<a id="configuration-gaming-pacman"></a>
###### pacman

```sh title='Run the following command'
sudo pacman -S proton-cachyos-slr
```

**Manual Installation (Advanced):**

1. Download the latest version [here.](https://github.com/CachyOS/proton-cachyos/releases) (`Scroll down to Assets`)
> **Note:**
> Choose the one that ends with `x86-64_v3` if your CPU supports **[AVX2](#installation-installation-prepare-x8664-microarchitecture-level-support)**
> Otherwise download the one ending with `x86-64`.
2. Decompress the file and move the folder to `~/.steam/steam/compatibilitytools.d/`
3. Restart Steam if you had it open.

<a id="configuration-gaming-wine-cachyos"></a>
### Wine-CachyOS

This is the same `wine` that is at the core of `proton-cachyos`, but as a standalone package. It can be used in Lutris, Heroic, Bottles and others.

- **All the Wine modifications included with Proton-CachyOS**
- **Adds early hotfixes/workarounds for games**

> **Note:**
> In the CachyOS repositories, **Wine-CachyOS** is offered by two different packages. `wine-cachyos` installs it as the default system Wine and replaces `wine` or `wine-staging`. `wine-cachyos-opt` installs it in a different location, which allows multiple wine versions to co-exist in the system.

> **Caution:**
> **Wine-CachyOS's** primarily intended use is for **gaming**. Although it can be used as a system Wine with desktop applications, be aware that it might lead to some unexpected behavior and issues due to the gaming focused modifications.
>
> If you want to use desktop application, we suggest using `wine` or `wine-staging` as your system's Wine and installing `wine-cachyos-opt` for gaming.

**Additional configuration options**

- `WINE_WMCLASS="&lt;name&gt;"`: Sets the `WM_CLASS` of all wine windows, allowing the window manager to control the Wine's windows through rules.
- `WINEUSERSANDBOX=1`: Disables the creation of symlinks from Wine user folders such as Documents/Pictures, to the equivalent folders in the user's `HOME` directory
- `WINE_NO_WM_DECORATION=1`: Disables window decorations using the Linux window manager. It can fix issues with **borderless fullscreen** and the mouse clicking through the window.
- `WINE_PREFER_SDL_INPUT=1`: Enable to work-around issues with proper controller detection.

<a id="configuration-gaming-how-to-use-wine-cachyos-opt"></a>
#### How to use wine-cachyos-opt

<a id="configuration-gaming-standalone"></a>
###### Standalone

Normally, running `/opt/wine-cachyos/bin/wine` instead of just `wine` should be enough for an application to run using `wine-cachyos-opt`.

If a more strict configuration is required, it could look like this:
    ```shell
    ```

If you want to use `winetricks` with `wine-cachyos-opt`, you can invoke it like this:
    ```shell
    WINE=/opt/wine-cachyos/bin/wine WINEPRFIX=&lt;your prefix&gt; winetricks &lt;verb&gt;
    ```

<a id="configuration-gaming-lutris"></a>
###### Lutris

> **Note:**
> The second image also applies for setting it up per game.
  ![Image](src/assets/images/lutris-guide-1.png)
![Image](src/assets/images/lutris-guide-2.png)

<a id="configuration-gaming-heroic-games-launcher"></a>
###### Heroic Games Launcher

  ![Image](src/assets/images/heroic-wine.png)
![Image](src/assets/images/heroic-wine-2.png)
![Image](src/assets/images/heroic-wine-3.png)

<a id="configuration-gaming-steam-faq-tips"></a>
### Steam FAQ & Tips

> **Note:**
> Laptop users with discrete NVIDIA GPUs should refer to the [Dual GPU Laptops guide](#configuration-dual-gpu)

> **Tip:**
> CachyOS provides various Proton versions that we build & maintain for further performance improvements:
> - `proton-cachyos` `(included in the cachyos-gaming-meta package)` is the one that we develop with added QoL changes + cherry picked patches + compilation optimizations `(x86-64-v3 & x86-64-v4)`

> **Tip:**
> To check if your game is compatible or how it runs with Linux, visit **[ProtonDB](https://www.protondb.com/)** or **[Are We Anti-Cheat Yet?](https://areweanticheatyet.com/).**

<a id="configuration-gaming-which-proton-version-should-be-used-in-steam"></a>
#### Which Proton version should be used in Steam?

- `Proton 10.0` is the stable release from `Valve`. Use this if the game you want to play is known to work well.
- `Proton Experimental` is the bleeding edge release from `Valve`. Use this if the game you want to play is relatively new, doesn't work well with the current Proton stable release, or if people recommend it on [ProtonDB](https://www.protondb.com/).
- `proton-cachyos-slr` is the one we build and maintain. Using it is highly recommended with various quality-of-life features, fixes and optimizations. For games using anticheat, such as **BattlEye** or **Easy Anti-Cheat** or custom launchers, prefer `proton-cachyos-slr`.
- `proton-cachyos` is the same version as `proton-cachyos-slr` but built without depending on the Steam Linux Runtime. Use it only if you understand the significance of this difference and fallback to `proton-cachyos-slr` if issues occur.
- `Proton-GE` is a custom build made by [GloriousEggroll](https://github.com/GloriousEggroll/proton-ge-custom). It includes various fixes, and can be useful to have in certain situations.
- `Proton 9.0.4 or lower` are the stable releases from `Valve`. Use this if the game you want to play only works in a previous Proton release.

<a id="configuration-gaming-fix-stuttering-caused-by-the-steam-game-recorder-feature"></a>
#### Fix stuttering caused by the Steam Game Recorder Feature

> **Caution:**
> Adding this environment variable causes **Steam's Overlay** to stop functioning.

```sh title='Add the following launch option to your game'
LD_PRELOAD="" %command%
```

<a id="configuration-gaming-capturing-and-sharing-proton-logs"></a>
#### Capturing and sharing Proton logs

> **Note:**
> When sharing logs with CachyOS, please upload them to **[paste-cachyos](https://paste.cachyos.org/)** instead of posting directly.
>
> You can simply drag and drop the log file onto the website, then share the generated link.

To enable Proton logging for a game:

1. Right-click your game in Steam and select **Properties**.
2. Under **Launch Options**, add the `PROTON_LOG` environment variable:
        ```sh
        PROTON_LOG=1 %command%
        ```
    This will create a log file in your home directory, named `steam-&lt;AppID&gt;.log` (for example, Counter Strike 2 uses AppID **730**, so the file would be `steam-730.log`).

**Custom Log Directory:**

To set a custom log directory, use `PROTON_LOG_DIR`:

```bash title='Example'
PROTON_LOG=1 PROTON_LOG_DIR=/home/cachyos/steam-logs %command%
```

<a id="configuration-gaming-pre-caching-shaders-with-proton-cachyos-ge-and-em"></a>
#### Pre-caching shaders with Proton-CachyOS, -GE and -EM

> **Note:**
> It's advised to disable the `Steam Precache of Shaders` feature when utilizing Proton-CachyOS, Proton-GE or Proton-EM. They already contain all the necessary codecs to play videos inside games, and nowadays a relatively modern GPU-CPU combo should be more than capable of dealing with compiling shaders in-game.
>
> But if you have time to spare, then you can ignore this tip and let Steam pre compile some shaders for your game.
>
> `Keep in mind that not everything gets cached during this process.`

**Here is how to disable this feature:**

![Image](src/assets/images/steam-setting.png)
![Image](src/assets/images/steam-shader-cache.png)

> **Note:**
> It's highly recommended to [increase your maximum shader cache size](#increase-maximum-shader-cache-size) after disabling pre-caching on Steam.

<a id="configuration-gaming-repurposing-a-windows-ntfs-game-partition"></a>
#### Repurposing a Windows NTFS game partition

> **Caution:**
> Avoid using Proton on NTFS drives. Valve does not support this configuration, and it can cause games to behave unpredictably.
>
> If you're willing to proceed. Follow their **[unofficial guide.](<https://github.com/ValveSoftware/Proton/wiki/Using-a-NTFS-disk-with-Linux-and-Windows>)**

<a id="configuration-gaming-lutrishttpslutrisnet"></a>
### [Lutris](<https://lutris.net/>)

Lutris serves as a central hub for all your games on CachyOS.

With Lutris, you can efficiently manage your game runners, including Wine, Proton, and emulators.

- **You can launch games through Lutris simply by clicking the Play button.**
- **Add any game you want clicking the + sign in the top left.**
- **Set up a store in the Sources at the left panel and connecting your account, it will then proceed to install said store, and then you'll be able to run games from within the store, just like you do on Windows.**
- **And more!**

*Games stores supported in Lutris:*

- [EA App](https://lutris.net/games/ea-app/)
- [Epic Games Store](https://lutris.net/games/epic-games-store/)
- [GOG Galaxy](https://lutris.net/games/gog-galaxy/)
- [Steam](https://lutris.net/games/steam/)
- [Ubisoft Connect](https://lutris.net/games/ubisoft-connect/)

<a id="configuration-gaming-how-to-properly-set-multiple-launch-options-and-environment-variables-in-lutris"></a>
#### How to properly set multiple launch options and environment variables in Lutris

- Launch options such as `-dx11` or `-fullscreen` should be added in the **Arguments** field under the **Game options** tab using a space as a separator.
- Command wrappers for example `mangohud --dlsym` or `game-performance` should be added in the **Command prefix** field under the **System options** tab using a space as a separator.
- Environment variables such as `PROTON_ENABLE_HDR=1` should be added in the **Environment variables** table under the **System options** tab using the `+` button to add a new entry.
> **Note – Do not include `=` in the Key field. It should only contain the variable name.:**

<a id="configuration-gaming-performance-misc-tips"></a>
### Performance & Misc tips

<a id="configuration-gaming-what-not-do-when-gaming-in-cachyos"></a>
#### What not do when Gaming in CachyOS

<a id="configuration-gaming-combining-gamemode-and-ananicy-cpp"></a>
##### Combining gamemode and ananicy-cpp

Due to `gamemode` and `ananicy-cpp` both trying to modify a process niceness at the same time, it can lead to conflicts and unexpected behavior. It's recommended to use gamemode without ananicy-cpp.

To stop ananicy-cpp, execute the following command:

```bash
systemctl stop ananicy-cpp
```

<a id="configuration-gaming-power-profile-switching-on-demand"></a>
#### Power Profile Switching on Demand

> **Note:**
> This behavior differs slightly with `intel_pstate`. On Intel, the governor stays at powersave, but the EPP/EPB values are adjusted for performance.

> **Caution – game-performance may not provide any benefit on old CPUs.:**

CachyOS includes a wrapper script [game-performance](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/bin/game-performance)
which uses `power-profiles-daemon` to temporarily switch the power profile to `performance`.
The profile raises system power levels and sets the CPU governor to `performance`.

When used to launch a game, the system remains in **performance mode** until the game exits, at which point the previous profile is restored.

[Feral's GameMode](https://github.com/FeralInteractive/gamemode)
offers similar functionality.

<a id="configuration-gaming-how-to-add-game-performance-to-steam-lutris-and-heroic-games-launcher"></a>
#### How to add game-performance to Steam, Lutris and Heroic Games Launcher

<a id="configuration-gaming-steam"></a>
###### Steam

1. Open your `Steam Library`.
2. Right click the game's title and select `Properties`.
3. On the `General` tab you'll find `Launch Options` section.
4. Add the following Launch Option:
    ```sh
    game-performance %command%
    ```

<a id="configuration-gaming-heroic-games-launcher"></a>
###### Heroic Games Launcher

1. On the left panel open `Settings`.
2. Go to `Game defaults` then click on `Advanced`.
3. In the `wrapper` command section. Add the following line without any argument:
   ```sh
   game-performance
   ```
4. Click on the `+` sign to save changes.

<a id="configuration-gaming-lutris"></a>
###### Lutris

1. On the top right open the `hamburger menu`.
2. Go to `Preferences/Global options`.
3. Enable `Advanced Mode` on the top right.
4. Scroll down to `Command prefix` and add the following line:
   ```sh
   game-performance
   ```
5. Save changes.

<a id="configuration-gaming-increase-maximum-shader-cache-size"></a>
#### Increase maximum shader cache size

Game shaders are compiled automatically while playing, which may cause long loading times and stuttering the first time you encounter them. These shaders are stored on your system to be re-used when needed.

However, there is a maximum limit to the shader cache's file size, causing old shaders to be forgotten when exceeding the default size. This can be an issue since large games can have shaders over 1GB in size, causing them to re-compile shaders every launch.

To avoid long loading times and stuttering, we can increase the global shader cache size:

<a id="configuration-gaming-nvidia-gpu"></a>
###### Nvidia GPU

1. Open the terminal.
2. Enter this command to edit the environment file:
	```sh
	sudo nano /etc/environment
	```
3. Paste the following at the end of the file:
	```sh
	# Increase Nvidia's shader cache size to 12GB
	__GL_SHADER_DISK_CACHE_SIZE=12000000000
	```
4. Save the file by pressing `CTRL+X`, `Y`, then `Enter`.
5. Restart your system.

<a id="configuration-gaming-amd-gpu"></a>
###### AMD GPU

1. Open the terminal.
2. Enter this command to edit the environment file:
	```sh
	sudo nano /etc/environment
	```
3. Paste the following at the end of the file:
	```sh
	# Enforces RADV Vulkan implementation
	AMD_VULKAN_ICD=RADV

	# Increase AMD's shader cache size to 12GB
	MESA_SHADER_CACHE_MAX_SIZE=12G
	```
4. Save the file by pressing `CTRL+X`, `Y`, then `Enter`.
5. Restart your system.

After restarting, the maximum shader cache size should be permanently increased. Thanks to [psygreg's shader booster](https://github.com/psygreg/shader-booster/) for helping this guide.

<a id="configuration-gaming-forcing-the-latest-dlss-preset"></a>
#### Forcing the latest DLSS preset

<a id="configuration-gaming-how-to-add-dlss-swapper-to-steam-lutris-and-heroic-games-launcher"></a>
##### How to add dlss-swapper to Steam, Lutris and Heroic Games Launcher

<a id="configuration-gaming-steam"></a>
###### Steam

1. Open your `Steam Library`
2. Right click the game's title and select `Properties`.
3. On the `General` tab you'll find `Launch Options` section.
4. Add the following Launch Option:
    ```sh
    dlss-swapper %command%
    ```

<a id="configuration-gaming-heroic-games-launcher"></a>
###### Heroic Games Launcher

1. On the left panel open `Settings`.
2. Go to `Game defaults` then click on `Advanced`.
3. In the `wrapper` command section. Add the following line without any argument:
   ```sh
   dlss-swapper
   ```
4. Click on the `+` sign to save changes.

<a id="configuration-gaming-lutris"></a>
###### Lutris

1. On the top right open the `hamburger menu`
2. Go to `Preferences/Global options`.
3. Enable `Advanced Mode` on the top right.
4. Scroll down to `Command prefix` and add the following line:
   ```sh
   dlss-swapper
   ```
5. Save changes.

**Manual DLL Replacement Method:**

If `dlss-swapper` is not working or causing issues try updating game's DLSS implementation manually by replacing `nvngx_dlss.dll` with an up-to-date version and using the `dlss-swapper-dll` wrapper script instead.

<a id="configuration-gaming-ray-tracing-support"></a>
#### Ray tracing Support
The Arch Wiki has already provides comprehensive instructions on how to enable [ray tracing](https://wiki.archlinux.org/title/Hardware_raytracing) for various hardware platforms.
- [Ray tracing on NVIDIA](https://wiki.archlinux.org/title/Hardware_raytracing#NVIDIA)
- [Ray tracing on AMD](https://wiki.archlinux.org/title/Hardware_raytracing#AMD)
- [Ray tracing on Intel](https://wiki.archlinux.org/title/Hardware_raytracing#Intel)

<a id="configuration-gaming-performance-drop-on-nvidia-in-directx12-games"></a>
#### Performance drop on NVIDIA in DirectX12 games

Some users report that the issue is related to how NVIDIA’s Linux drivers handle GPU scheduling—unlike on Windows, where proper scheduling is enforced. There’s no official NVIDIA statement yet. Currently there is no known workaround for this issue and NVIDIA is supposedly working on a fix but it's not clear when it will be released.

**It has nothing to do with CachyOS.**

In some titles the performance drop is less noticeable than in others. Check out this [benchmark comparison video](https://www.youtube.com/watch?v=SU2mFqCOh5A) for reference.

Follow the [NVIDIA thread](https://forums.developer.nvidia.com/t/directx12-performance-is-terrible-on-linux/303207/488) about this issue to know more about it.

<a id="configuration-general-system-tweaks"></a>
#### General System Tweaks

<a id="configuration-general-system-tweaks-amd-performance-tweaks"></a>
### AMD Performance Tweaks

<a id="configuration-general-system-tweaks-amd-p-state-driver"></a>
#### AMD P-State Driver
---------------------------

`amd-pstate` is the AMD CPU performance scaling driver that introduces a new CPU frequency control mechanism on modern AMD APU and CPU series in the Linux kernel. The new mechanism is based on Collaborative Processor Performance Control (CPPC) which provides finer grain frequency management than legacy ACPI hardware P-States.

Current AMD CPU/APU platforms are using the ACPI P-states driver to manage CPU frequency and clocks with switching only in 3 P-states. CPPC replaces the ACPI P-states controls and allows a flexible, low-latency interface for the Linux kernel to directly communicate the performance hints to hardware.

Below are 3 operation modes of the `amd-pstate` driver and kernel cmdline entries to use them on boot:

- AMD P-State (Non-Autonomous Mode): `amd-pstate=passive`
- AMD P-State Guided (Guided Autonomous Mode): `amd-pstate=guided`
- AMD P-State EPP (Autonomous Mode): `amd-pstate=active`

> **Note:**
> The AMD P-State EPP Driver is used by default when no explicit configuration is made.

You can also switch between operation modes at runtime to test the options:

- **Autonomous mode**: platform considers only the values set for Minimum performance, Maximum performance, and Energy Performance Preference.
   ```sh
   echo active | sudo tee /sys/devices/system/cpu/amd_pstate/status
   ```

- **Guided-autonomous mode**: platform sets operating performance level according to the current workload and within limits set by the OS through minimum and maximum performance registers.
   ```sh
   echo guided | sudo tee /sys/devices/system/cpu/amd_pstate/status
   ```

- **Non-autonomous mode**: platform gets desired performance level from OS directly through Desired Performance Register.
   ```sh
   echo passive | sudo tee /sys/devices/system/cpu/amd_pstate/status
   ```

For more information:

*   [https://www.kernel.org/doc/html/v6.9/admin-guide/pm/amd-pstate.html](https://www.kernel.org/doc/html/v6.9/admin-guide/pm/amd-pstate.html)
*   [https://lore.kernel.org/lkml/20221110175847.3098728-1-Perry.Yuan@amd.com/](https://lore.kernel.org/lkml/20221110175847.3098728-1-Perry.Yuan@amd.com/)
*   [https://lore.kernel.org/lkml/20230119115017.10188-1-wyes.karny@amd.com/](https://lore.kernel.org/lkml/20230119115017.10188-1-wyes.karny@amd.com/)

<a id="configuration-general-system-tweaks-configuring-amd-p-state-epp"></a>
#### Configuring AMD P-State EPP

To use the P-State EPP, there are two CPU frequency scaling governors available: `powersave` and `performance`. It is recommended to use the powersave governor and set a preference.

*   Set powersave governor: `sudo cpupower frequency-set -g powersave`
*   Set performance governor: `sudo cpupower frequency-set -g performance`

To set a preference, run the following command with the desired preference:

```sh
echo power | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference
```

Available preferences: `performance`, `power`, `balance_power`, `balance_performance`

Benchmarks for each preference can be found here:
[https://lore.kernel.org/lkml/20221219064042.661122-1-perry.yuan@amd.com/](https://lore.kernel.org/lkml/20221219064042.661122-1-perry.yuan@amd.com/)

<a id="configuration-general-system-tweaks-amd-3d-v-cache-optimizer"></a>
#### AMD 3D V-Cache Optimizer

AMD posted a patch to optimize the Cache Scheduling on Dual CCD 3D CPUs, like 7950X3D and 7900X3D.
You need to set in the BIOS under the CPPC Option to the "Driver" Option. This will allow to override with the sysfs the used mode.

There are two modes:
1. Frequency
2. Cache

If `cache` is set, the driver will try to put the tasks first on the CCD with the higher Cache, this is mainly profitable on games.
The `frequency` option will try to put the tasks on the second CCD, which has a higher frequency than the 3D Cache CCD.

Frequency (Default):
```sh
echo frequency | sudo tee /sys/bus/platform/drivers/amd_x3d_vcache/AMDI0101:00/amd_x3d_mode
```

Cache:
```sh
echo cache | sudo tee /sys/bus/platform/drivers/amd_x3d_vcache/AMDI0101:00/amd_x3d_mode
```

After you changed the modes, the amd preferred core stats should provide a different ranking. You can read it out with:
```sh
grep -v /sys/devices/system/cpu/cpu*/cpufreq/amd_pstate_prefcore_ranking
```

<a id="configuration-general-system-tweaks-amd-p-state-core-performance-boost"></a>
#### AMD P-State Core Performance Boost

AMD Core Performance Boost aka AMD Turbo Core is a dynamic frequency scaling technology by AMD that allows the
processor to dynamically adjust and control the processor operating frequency in certain version of its processors
which allows for increased performance when needed while maintaining lower power and thermal parameters during normal operation.

Since `linux-cachyos` 6.9.6, the kernel is patched with CPB support for AMD's p-state drivers (includes `passive`, `active` and `guided`).
Users can change each CPU's boost state via the sysfs boost file `/sys/devices/system/cpu/cpuX/cpufreq/boost`
(X refers to the core number e.g. cpu0 is the first core, cpu1 second, etc).

```sh
❯ echo 0 | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/boost # Disable boost for all cores
❯ lscpu -ae # This shows that AMD CPB is disabled globally
CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE    MAXMHZ   MINMHZ       MHZ
  0    0      0    0 0:0:0:0          yes 3301.0000 400.0000 1212.8250
  1    0      0    0 0:0:0:0          yes 3301.0000 400.0000 1394.2180
  2    0      0    1 1:1:1:0          yes 3301.0000 400.0000 1204.4600

❯ echo 1 | sudo tee /sys/devices/system/cpu/cpu0/cpufreq/boost # Enables boost on cpu0
❯ lscpu -ae
CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE    MAXMHZ   MINMHZ       MHZ
  0    0      0    0 0:0:0:0          yes 4564.0000 400.0000 1393.2380
  1    0      0    0 0:0:0:0          yes 3301.0000 400.0000  400.0000
  2    0      0    1 1:1:1:0          yes 3301.0000 400.0000 2157.8469
```

CachyOS also provides a version of `power-profiles-daemon` that backports a commit which enables
support for AMD CPB. AMD CPB will be disabled if the `powersave` profile is being used, and will be enabled on `balanced` or `performance`.

For more information see:
- https://lore.kernel.org/linux-pm/1a78eeaa-fadd-4734-aaeb-2fe11e96e198@amd.com/T/#m4a0c8917ea8fb033504055bd61512c80c85410c8
- https://lore.kernel.org/linux-pm/20240624213400.67773-1-mario.limonciello@amd.com/

<a id="configuration-general-system-tweaks-performance-improvements"></a>
### Performance Improvements

<a id="configuration-general-system-tweaks-disabling-split-lock-mitigate"></a>
#### Disabling Split Lock Mitigate

> **Note:**
> Split Lock Mitigation is now disabled by default when installing the `cachyos-gaming-meta` package.

In some cases, split lock mitigate can slow down performance in some applications and games. A patch is available to disable it via sysctl.

*   Disable split lock mitigate: `sudo sysctl kernel.split_lock_mitigate=0`
*   Enable split lock mitigate: `sudo sysctl kernel.split_lock_mitigate=1`

To make the change persistent, add the following line to `/etc/sysctl.d/99-splitlock.conf`:

```text
kernel.split_lock_mitigate=0
```

For more information on split lock, see:

- https://www.phoronix.com/news/Linux-Splitlock-Hurts-Gaming
- https://github.com/doitsujin/dxvk/issues/2938

<a id="configuration-general-system-tweaks-adios-io-schedulerhttpsgithubcomfirelzrdadios"></a>
#### [ADIOS I/O Scheduler](https://github.com/firelzrd/adios)

Created by [firelzrd](https://github.com/firelzrd)

> **Note:**
> CachyOS includes the stable branch of ADIOS in the kernel.
>
> Current version in **linux-cachyos**: `3.1.6`
>
> Current version in **linux-cachyos-rc**: `3.1.6`

Brief introduction from README:

- *ADIOS (Adaptive Deadline I/O Scheduler) is a block layer I/O scheduler for the Linux kernel, designed for modern multi-queue block devices (blk-mq). It aims to provide low latency for I/O operations by combining deadline scheduling principles with a learning-based adaptive latency control mechanism.*
- *Inspired by and builds upon concepts from the mq-deadline and Kyber I/O schedulers. Its core feature is the ability to predict I/O completion latency based on past performance and request characteristics (operation type, size) and use this prediction to dynamically adjust request deadlines and batching behavior.*

TLDR: ADIOS works by learning the latency profile of your storage device and using that knowledge to dynamically set deadlines for I/O requests. It prioritizes requests into four tiers, from critical system operations (Tier 0) to background tasks (Tier 3), to ensure a smooth user experience. While it focuses on responsiveness, its behavior can be fine-tuned via sysfs settings to balance latency and throughput.

For a live demo, you can watch this [video](https://www.youtube.com/watch?v=L9WDcEeHgy4)

<a id="configuration-general-system-tweaks-how-to-enable-adios"></a>
##### How to enable ADIOS

<a id="configuration-general-system-tweaks-temporarily-takes-effect-at-runtime"></a>
###### Temporarily (takes effect at runtime)

    This method sets the scheduler for the current session. The change will be lost on reboot.
        ```sh
        sync && echo adios | sudo tee /sys/block/&lt;yourdrive&gt;/queue/scheduler
            # Replace &lt;yourdrive&gt; with the actual drive identifier (e.g. sda, sdb, nvme0n1)
        ```

<a id="configuration-general-system-tweaks-persistent-after-reboot"></a>
###### Persistent after reboot

    
        1. Open or create a new udev rules file in your preferred text editor (e.g., nano, micro, vim)
                ```sh title='Example'
                sudo nano /etc/udev/rules.d/60-ioschedulers.rules
                ```
        2. Add the following rules to the file. These rules automatically apply a specific I/O scheduler based on the drive type (HDD, SSD, or NVMe).
                ```text
                # HDD
                ACTION=="add|change", KERNEL=="sd[a-z]*", ATTR{queue/rotational}=="1", \
                    ATTR{queue/scheduler}="bfq"

                # SSD
                ACTION=="add|change", KERNEL=="sd[a-z]*|mmcblk[0-9]*", ATTR{queue/rotational}=="0", \
                    ATTR{queue/scheduler}="adios"

                # NVMe SSD
                ACTION=="add|change", KERNEL=="nvme[0-9]*", ATTR{queue/rotational}=="0", \
                    ATTR{queue/scheduler}="adios"
                ```
          3.  Save the file and close the editor.
          4.  Reload the `udev` rules to apply the changes immediately without a reboot.
                  ```sh
                  sudo udevadm control --reload-rules
                  sudo udevadm trigger
                  ```
    

FAQ:

- If it improves responsiveness, why isn't it enabled by default?
- ADIOS is still under active development and continuous testing. While it offers significant benefits for desktop responsiveness, it is not yet considered stable enough to be the default for all workloads and hardware types. In some edge cases, bugs could lead to issues like system lockups. For this reason, it is an optional feature for users who wish to test and benefit from its latest improvements.

<a id="configuration-general-system-tweaks-power-saving-tweaks"></a>
### Power Saving Tweaks

<a id="configuration-general-system-tweaks-enable-rcu-lazy"></a>
#### Enable RCU Lazy

RCU Lazy helps reducing the power usage at idle or lightly loaded systems. This can be useful for laptops and handheld devices.
The improvement is between 5-10% in terms of power savings. However, it's important to note that this power saving feature may come at the cost of slightly reduced performance depending on the scenario.
The linux-cachyos-deckify kernel will have this option enabled by default, since power saving is key and necessary for these devices.

To enable RCU Lazy, add the following parameter to your kernel [cmdline](#configuration-boot-manager-configuration) parameters list:
```text
rcutree.enable_rcu_lazy=1
```

<a id="configuration-general-system-tweaks-nvidia-troubleshooting"></a>
### NVIDIA Troubleshooting

<a id="configuration-general-system-tweaks-disabling-sddm-wayland-backend"></a>
#### Disabling SDDM Wayland Backend

> **Note:**
> Starting from cachyos-kde-settings 4.3, SDDM uses KWin as it's Wayland compositor by default.

While this a nice step forward, it might introduce some annoyances such as breaking support for overclocking using nvidia-settings or cause incompatibility with older GPUs which struggle under Wayland.

In order to revert this change. Remove the cachyos-kde-settings package:
```sh
sudo pacman -R cachyos-kde-settings
```

<a id="configuration-general-system-tweaks-nvidia-gsp-firmware"></a>
#### NVIDIA GSP Firmware

The NVIDIA GSP Firmware can **"in some cases"** lead to decreased performance. While the 555.58.02 NVIDIA Driver has largely addressed this issue, it may persist on certain systems.
If you are facing hiccups in KDE or bad performance in some cases, you can disable the GSP Firmware with the following config file:
`/etc/modprobe.d/nvidia-gsp.conf`

```text
options nvidia NVreg_EnableGpuFirmware=0
```

After creating the file, execute the following command:
```sh
sudo mkinitcpio -P
```

> **Note:**
> NVIDIA's [open kernel modules](https://github.com/NVIDIA/open-gpu-kernel-modules) are based on GSP firmware. Due to this, GSP cannot be disabled and this modprobe option will be ignored when using them. Use `linux-cachyos-nvidia` or `nvidia-dkms`.

It's generally recommended to test the GSP firmware after each new NVIDIA driver installation, as it often introduces beneficial features. Moreover, NVIDIA primarily started conducting QA testing using the GSP firmware.

<a id="configuration-general-system-tweaks-audio-and-software-enhancements"></a>
### Audio and Software Enhancements

<a id="configuration-general-system-tweaks-enhancing-laptop-speaker-sound"></a>
#### Enhancing Laptop Speaker Sound

Laptop speakers often produce thin and underwhelming sound due to their compact size and limited hardware capabilities. [EasyEffects](https://wiki.archlinux.org/title/PipeWire#EasyEffects) can significantly enhance the sound quality of your laptop's built-in speakers by applying various audio effects and custom configurations.

To get started you need to install EasyEffects and the required dependencies:

```bash
# Install EasyEffects
sudo pacman -S easyeffects
# Install additional plugins for more effects
sudo pacman -S lsp-plugins-lv2
sudo pacman -S zam-plugins
sudo pacman -S calf
sudo pacman -S mda.lv2
```

<a id="configuration-general-system-tweaks-configuration"></a>
##### Configuration

Follow these steps to configure EasyEffects:

1. Launch EasyEffects from your application menu or by typing `easyeffects` in the terminal.
2. Navigate to the **Output** tab to manage effects applied to your speaker audio.
3. Switch to the **Effects** tab to add, modify, or adjust audio effects.

![Image](src/assets/images/easyeffects.png)

<a id="configuration-general-system-tweaks-using-community-presets"></a>
###### Using Community Presets

For a quick and effective setup, start with **community-created presets** tailored for various audio scenarios:

1. Download presets from the [EasyEffects Community Presets](https://github.com/wwmm/easyeffects/wiki/Community-presets) repository.
2. In EasyEffects, click the **Presets** button and choose **"Import preset from local storage"**.
3. Locate and select the downloaded preset file.
4. Once imported, the preset will appear in your list—click **"Load"** to apply it to your audio output.

![Image](src/assets/images/easyeffects-presets.png)

<a id="configuration-general-system-tweaks-creating-a-custom-profile"></a>
###### Creating a Custom Profile

For a more personalized audio experience, create a custom profile tailored to your laptop's speakers:

1. Click the **"+"** button in the Presets menu to create a new preset (e.g., name it **"Laptop Speakers"**).
2. Select **"Load"** to activate the new preset.
3. Add and configure effects in the **Output** > **Effects** tab, experimenting with options like equalizers, bass enhancers, or stereo wideners.

<a id="configuration-general-system-tweaks-using-the-convolver-effect-dolby-atmos-laptops"></a>
###### Using the Convolver Effect (Dolby Atmos Laptops)

The **Convolver effect** can dramatically improve sound by applying impulse responses that simulate high-quality audio environments. However, it requires precise setup:

1. Add the **Convolver** effect to your effects chain in the **Effects** tab.
2. Load an impulse response file (in `.wav` format) specific to your laptop model, if available. You can search for these files online at resources like:
- https://wiki.archlinux.org/title/Lenovo_ThinkPad_T14_(AMD)_Gen_4#Speakers
- https://github.com/m4tx/thinkpad-p14s-g4-linux/#sound
- https://github.com/shuhaowu/linux-thinkpad-speaker-improvements/
3. **Prevent clipping**: The Convolver effect may increase volume significantly. Add a **Limiter** effect after the Convolver in your effects chain to control peaks and avoid distortion.

![Image](src/assets/images/easyeffects-convolver.png)

<a id="configuration-general-system-tweaks-tips-for-optimal-results"></a>
##### Tips for Optimal Results

- **Experiment** with different presets to identify the best match for your specific laptop model and personal sound preferences.
- **Make incremental adjustments** to individual effects to prevent distortion or unnatural sound output.
- **Compare with toggle**: Frequently toggle EasyEffects **on/off** to evaluate the improvements against the default audio.
- Search for **device-specific presets or Convolver impulse responses** for popular laptop models like **Framework Laptop 13** or **ThinkPad T14** to achieve tailored results.
- **Automate startup**: Configure EasyEffects to launch automatically at startup through the app's preferences to ensure your custom profile is always applied.
- **Autoload presets for multiple devices**: Use the **PipeWire** > **Presets Autoloading** tab to associate specific presets with different output devices (e.g., Speakers vs. Headphones) for seamless switching. ![Image](src/assets/images/easyeffects-autoloading.png)

<a id="configuration-general-system-tweaks-alternative-to-easyeffects"></a>
##### Alternative to EasyEffects

As an alternative you can try using [JDSP4Linux](https://github.com/Audio4Linux/JDSP4Linux), which is an audio effect processor for PipeWire and PulseAudio clients.

<a id="configuration-general-system-tweaks-obs-studio"></a>
#### OBS Studio

We provide a custom obs-studio-browser package in our repository that is recommended over the standard `obs-studio` package. It contains patches to fix some of the common issues like cuda-errors and virtual camera problems.

```sh title='Open a terminal and run the following command'
sudo pacman -S obs-studio-browser
# If you previously had the obs-studio installed then pacman is going to ask you if
# you want to replace it, if so enter "Y".
```

<a id="configuration-post-install-setup"></a>
#### Post Install

<a id="configuration-post-install-setup-updating-the-system"></a>
### Updating The System

<a id="configuration-post-install-setup-using-octopi-gui"></a>
###### Using Octopi (GUI)

Octopi is a graphical package manager for Arch-based distributions that provides a convenient way to manage packages and updates.
To update your system with Octopi, follow these steps:

1. Launch **Octopi** from the application menu.
2. In the main window, click on the **Check updates** button (Top left), now next to it **System upgrade.**
3. Octopi will now check for available updates and prompt you to either install them on Octopi itself or in a terminal.
4. To proceed with the update, click the **Apply** button.
5. Octopi will download and install the updates.
6. It is advised to reboot your computer after a big update **(especially if the kernel got an update)**.

<a id="configuration-post-install-setup-using-pacman"></a>
###### Using Pacman

1. Open a terminal emulator (or press `ctrl + alt + t` - `mod + return` in a WM e.G Qtile).
2. Run the following command to update the system:

   ```sh
   sudo pacman -Syu
   ```
3. It is advised to reboot your computer after a big update **(especially if the kernel got an update)**.

<a id="configuration-post-install-setup-offline-system-update"></a>
###### Offline System Update

*CachyOS supports offline system upgrades using the [`pacman-offline`](https://github.com/eworm-de/pacman-offline) script. This allows your system to download package updates and apply them on the next reboot. (Yes like on Windows)*

> **Note:**
> The `pacman-offline` tool integrates with systemd's offline updates feature. It automatically handles kernel updates and module loading.
>
> The `/etc/pacman.d/offline.conf` file is crucial for managing which packages are updated during regular and offline updates. Ensure it's configured correctly for your desired kernel or add the packages you want so they only get updated during the pacman-offline execution and get ignored in a regular update. Example: `pacman -Syu`.
>
> **If you enable the automatic update timer, you no longer need to manually update your system.**

1. **Install the pacman-offline package**

   ```bash
   sudo pacman -S pacman-offline
   ```

2. **Telling Pacman to read from the separate package ignore list.**

> **Note – Add the line after the [options:**

   ```bash title='Add the following line to the /etc/pacman.conf file'
   Include = /etc/pacman.d/offline.conf
   ```
   *Example*
   ```bash
   # /etc/pacman.conf
   # REPOSITORIES
   #   - can be defined here or included from another file
   #   - pacman will search repositories in the order defined here
   #   - local/custom mirrors can be added here or in separate files
   #   - repositories listed first will take precedence when packages
   #     have identical names, regardless of version number
   #   - URLs will have $repo replaced by the name of the current repo
   #   - URLs will have $arch replaced by the name of the architecture
   #
   # Repository entries are of the format:
   #       [repo-name]
   #       Server = ServerName
   #       Include = IncludePath
   #
   # The header [repo-name] is crucial - it must be present and
   # uncommented to enable the repo.
   #
   # GENERAL OPTIONS
   [options]
   # other options like 'Color', 'CheckSpace', etc. can be here
   Include = /etc/pacman.d/offline.conf
   ```
3. **Adding the CachyOS kernels in order to make pacman ignore them during regular updates**

   The `pacman-offline` tool uses this file to determine which packages to ignore during the traditional pacman updates.

   Example: when you run `sudo pacman -Syu`

   *Replace the contents of the `/etc/pacman.d/offline.conf` file with the following:*

   ```text
   # Arch Linux kernels
   IgnorePkg = linux linux-headers linux-docs
   IgnorePkg = linux-lts linux-lts-headers linux-lts-docs
   IgnorePkg = linux-zen linux-zen-headers linux-zen-docs
   IgnorePkg = linux-hardened linux-hardened-headers linux-hardened-docs

   # CachyOS kernels
   IgnorePkg = linux-cachyos linux-cachyos-headers
   IgnorePkg = linux-cachyos-bmq linux-cachyos-bmq-headers
   IgnorePkg = linux-cachyos-bore linux-cachyos-bore-headers
   IgnorePkg = linux-cachyos-deckify linux-cachyos-deckify-headers
   IgnorePkg = linux-cachyos-eevdf linux-cachyos-eevdf-headers
   IgnorePkg = linux-cachyos-gcc linux-cachyos-gcc-headers
   IgnorePkg = linux-cachyos-hardened linux-cachyos-hardened-headers
   IgnorePkg = linux-cachyos-lts linux-cachyos-lts-headers
   IgnorePkg = linux-cachyos-rc linux-cachyos-rc-headers
   IgnorePkg = linux-cachyos-rt-bore linux-cachyos-rt-bore-headers
   IgnorePkg = linux-cachyos-server linux-cachyos-server-headers
   IgnorePkg = linux-cachyos-lto linux-cachyos-lto-headers
   IgnorePkg = linux-cachyos-bmq-lto linux-cachyos-bmq-lto-headers
   IgnorePkg = linux-cachyos-bore-lto linux-cachyos-bore-lto-headers
   IgnorePkg = linux-cachyos-deckify-lto linux-cachyos-deckify-lto-headers
   IgnorePkg = linux-cachyos-eevdf-lto linux-cachyos-eevdf-lto-headers
   IgnorePkg = linux-cachyos-gcc-lto linux-cachyos-gcc-lto-headers
   IgnorePkg = linux-cachyos-hardened-lto linux-cachyos-hardened-lto-headers
   IgnorePkg = linux-cachyos-lts-lto linux-cachyos-lts-lto-headers
   IgnorePkg = linux-cachyos-rc-lto linux-cachyos-rc-lto-headers
   IgnorePkg = linux-cachyos-rt-bore-lto linux-cachyos-rt-bore-lto-headers
   IgnorePkg = linux-cachyos-server-lto linux-cachyos-server-lto-headers
   ```

   *Now all of those packages are going to get ignored in the regular updates but checked during the offline preparation.*

3. **Start the preparation for the offline update only once**

   ```bash title='Run the following command'
   sudo systemctl start pacman-offline-prepare.service
   ```
   This command will then make pacman-offline to execute once and synchronize the package databases and proceed to download updates but doesn't install them.

*If you want this script to be automated. Follow the following steps:*

1. **Enable the preparation timer**

   The `pacman-offline-prepare.timer` being enabled will allow systemd to trigger this script to download updates in a daily basis after a few minutes of every system startup.

   ```bash
   sudo systemctl enable pacman-offline-prepare.timer
   ```

2. **Reboot your system:**

   The updates will be installed during the next system reboot.

3. **(Optional) Automatic System Reboots:**

Enable the `pacman-offline-reboot.timer` to automatically reboot your system by default at **3am** (Your timezone) if they're pending updates. Be aware that its not always at the same time schedule due to the inclusion of `RandomizedDelaySec` which is set to 2 hours by default.

    ```bash
    sudo systemctl enable pacman-offline-reboot.timer
    ```

> **Tip:**
> You can edit the `pacman-offline-reboot.timer` file to either modify at what time you want your system to reboot if they're is any pending update or disable the randomized schedule.

<a id="configuration-post-install-setup-cachy-update"></a>
###### Cachy-Update

Fork of [Arch-Update](https://github.com/Antiz96/arch-update)

An update notifier & applier for Arch Linux that assists you with important pre / post update tasks.
Includes a dynamic & clickeable systray applet for an easy integration with any Desktop Environment / Window Manager.

Enable Cachy-Update in CachyOS Hello > Apps/Tweaks > Cachy Update enabled

- Features:
- Automatic check and listing of available updates.
- Check for recent Arch Linux news (and offers to display them if there are).
- Check for orphan packages (and offers to remove them if there are).
- Check for old & uninstalled packages in cache (and offers to remove them if there are).
- Check for pending kernel update requiring a reboot (and offers to do so if there's one).
- Check for services requiring a post upgrade restart (and offers to do so if there are).
- Support for `sudo`, `sudo-rs`, `doas` & `run0`.

**Update check interval:** `Once 15 seconds after boot and then every hour.`

- How to change the update check interval:

```sh title='Run the following command'
systemctl --user edit --full arch-update.timer
# Tip: You can also use any text editor of your choice instead of `nano`
# e.g EDITOR=micro systemctl --user edit --full arch-update.timer
```
Default contents of the file:
```systemd
[Timer]
OnStartupSec=15 # Check for updates 15 seconds after boot
OnUnitActiveSec=1h # Check for updates every hour
```

Basically you can change the `OnUnitActiveSec` value to whatever you want. For example, if you want to check for updates every 30 minutes, change it to `30m`. or every 6 hours, change it to `6h`. Check this [document](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#Parsing%20Time%20Spans) for more details on how to set the time interval.

In case you want Cachy-Update to check for new updates only once at boot, you can simply delete the `OnUnitActiveSec` line completely.

Thanks to [Antiz](https://github.com/Antiz96) for maintaining the upstream Arch-Update project and for the implementation of Cachy-Update

<a id="configuration-post-install-setup-configuring-firewall-ufw"></a>
### Configuring Firewall (ufw)
> **Note:**
> UFW is enabled by default after installation.
To configure ufw, follow these steps:

<a id="configuration-post-install-setup-enable"></a>
###### Enable

```bash
sudo ufw enable
```

<a id="configuration-post-install-setup-disable"></a>
###### Disable

```bash
sudo ufw disable
```

<a id="configuration-post-install-setup-allow"></a>
###### Allow

By default, ufw allows all incoming and outgoing traffic, you can add specific rules to the firewall to block or allow specific connections.

```bash
# For example:
sudo ufw allow ssh
```

<a id="configuration-post-install-setup-deny"></a>
###### Deny

```bash
# To deny a specific port, check the following example:
sudo ufw deny 80
```

<a id="configuration-post-install-setup-status"></a>
###### Status

```bash
sudo ufw status verbose
```

> **Note:**
> Be careful when configuring firewall rules, as improperly configured rules can lock you out of your own system.

> **Note:**
> You can also configure it graphically using "Firewall" section in the KDE Plasma settings.

<a id="configuration-post-install-setup-configure-wi-fi-regulatory-domain"></a>
### Configure Wi-Fi Regulatory Domain

The `wireless-regdb` package includes a database of wireless rules (allowed frequencies, channels, power limits) for various countries. Setting the right region for your location can unlock specific Wi-Fi channels (such as channels 12/13 or 5GHz/6GHz bands) that may be limited by default, helping to improve your Wi-Fi performance and connection quality.

**Configuration:**

1. Edit the configuration:
   Open `/etc/conf.d/wireless-regdom` with root privileges.
   ```bash
   sudo micro /etc/conf.d/wireless-regdom
   ```
2. Set your country:
   Uncomment the line with your two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) (e.g., `WIRELESS_REGDOM="US"`). Ensure only one country is uncommented.
3. Reboot:
   A reboot is typically required for the change to take effect.

**Verification:**

To check the currently applied regulatory domain, use this command:

```bash
iw reg get
global
country 00: DFS-UNSET # Country 00 uses global defaults
	(755 - 928 @ 2), (N/A, 20), (N/A), PASSIVE-SCAN
	(2402 - 2472 @ 40), (N/A, 20), (N/A)
	(2457 - 2482 @ 20), (N/A, 20), (N/A), AUTO-BW, PASSIVE-SCAN
	(2474 - 2494 @ 20), (N/A, 20), (N/A), NO-OFDM, PASSIVE-SCAN
	(5170 - 5250 @ 80), (N/A, 20), (N/A), AUTO-BW, PASSIVE-SCAN
	(5250 - 5330 @ 80), (N/A, 20), (0 ms), DFS, AUTO-BW, PASSIVE-SCAN
	(5490 - 5730 @ 160), (N/A, 20), (0 ms), DFS, PASSIVE-SCAN
	(5735 - 5835 @ 80), (N/A, 20), (N/A), PASSIVE-SCAN
	(57240 - 63720 @ 2160), (N/A, 0), (N/A)
```

Look for the `country XX:` line, where `XX` should match the code you set. If it shows `country 00:`, the system might be using default restrictions or hasn't yet determined the region.

```bash
iw reg get
global
country US: DFS-FCC # Country correctly shows as US
	(902 - 904 @ 2), (N/A, 30), (N/A)
	(904 - 920 @ 16), (N/A, 30), (N/A)
	(920 - 928 @ 8), (N/A, 30), (N/A)
	(2400 - 2472 @ 40), (N/A, 30), (N/A)
	(5150 - 5250 @ 80), (N/A, 23), (N/A), AUTO-BW
	(5250 - 5350 @ 80), (N/A, 24), (0 ms), DFS, AUTO-BW
	(5470 - 5730 @ 160), (N/A, 24), (0 ms), DFS
	(5730 - 5850 @ 80), (N/A, 30), (N/A), AUTO-BW
	(5850 - 5895 @ 40), (N/A, 27), (N/A), NO-OUTDOOR, AUTO-BW, PASSIVE-SCAN
	(5925 - 7125 @ 320), (N/A, 12), (N/A), NO-OUTDOOR, PASSIVE-SCAN
	(57240 - 71000 @ 2160), (N/A, 40), (N/A)
```

<a id="configuration-post-install-setup-enabling-global-menu"></a>
### Enabling Global Menu
For some apps like Visual Studio Code, the global menu may not work or may be attached to the parent app instead of the panel.

```sh
# To enable global menu support, run the command and restart the app.
sudo pacman -S appmenu-gtk-module libdbusmenu-glib
```

<a id="configuration-post-install-setup-enable-apparmor-support-using-apparmord-profiles-optional"></a>
### Enable AppArmor support using AppArmor.d profiles (Optional)

1. Add the following kernel parameters to your Boot Manager, see [Boot Manager Configuration](#configuration-boot-manager-configuration) for reference

   ```text
   lsm=landlock,lockdown,yama,integrity,apparmor,bpf
   ```

2. Install apparmor and apparmord **(Set of over +1500 profiles)** packages
   ```bash
   sudo pacman -S apparmor apparmor.d-git
   ```

3. Enable/Start AppArmor service

   ```bash
   systemctl enable --now apparmor.service
   ```

4. Enable caching for AppArmor profiles

   ```shell
   # /etc/apparmor/parser.conf
   ## Add the following lines:
   write-cache
   Optimize=compress-fast
   ```
   Save the file and reboot.

<a id="configuration-post-install-setup-changing-the-default-shell"></a>
### Changing the Default Shell

Currently, CachyOS uses [fish](https://fishshell.com/) as the user's default login shell. However, you can change
the default shell to whatever you like.

   
<a id="configuration-post-install-setup-bash"></a>
###### bash

  This is the default shell on almost every Linux distribution. It is also still used as the root user's login shell. bash
  has basic autocomplete functionality and easy history management. It differs from zsh and fish in that it doesn't have
  the fancy customization and plugin ecosystem that both fish and zsh have.

      ```sh title='Changing your default shell to bash'
      chsh -s /usr/bin/bash
      ```

   

   
<a id="configuration-post-install-setup-zsh"></a>
###### zsh

  We provide a [zsh config](https://github.com/CachyOS/cachyos-zsh-config) with commonly used plugins and configurations.
  It aims to have 1:1 functionality with our [fish config](https://github.com/CachyOS/cachyos-fish-config).
  This is also the default shell used in MacOS.

      ```sh title='Changing the default shell to zsh'
      chsh -s /usr/bin/zsh
      ```

   

<a id="configuration-post-install-setup-updatingusing-tldrhttpsgithubcomtldr-pagestldr"></a>
### Updating/using [tldr](https://github.com/tldr-pages/tldr)

> **Note:**
> CachyOS uses [tealdeer](https://github.com/tealdeer-rs/tealdeer) which is a faster Rust based implementation of the original tldr

This tool is extremely useful for those who don't want to read much or waste time reading a help/man page.

1. ```sh title="Open a terminal and run the following command"
   tldr --update
   ```
2. Example of using tldr:
   ```sh
   tldr java
 Execute a `.jar` program:

  java -jar filename.jar

<a id="configuration-post-install-setup-as-you-can-see-its-really-useful-and-new-toolspages-get-added-over-time"></a>
## As you can see, it's really useful, and new tools/pages get added over time.
   ```

## Managing Appimages

Appimages are portable applications that run on most Linux distributions without needing installation or root permissions.

> **Note – All AppImages require executable permissions to run.:**
> You can set the executable permission using the following command:
> ```sh
> chmod +x /path/to/your/appimage
> ```
> Or right click the AppImage file, go to `Properties` > `Permissions`, and check the box that says `Allow executing file as program.`

> **Note – Before running AppImages, ensure that FUSE (Filesystem in Userspace) is installed on your system.:**
> ```sh
> sudo pacman -S fuse2
> ```

To manage AppImages, you can use [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher), which provides an easy way to integrate AppImages into your system.

  
##### Using AppImageLauncher (GUI)

    AppImageLauncher is a graphical tool that simplifies the management of AppImages on your system. It integrates with your desktop environment, making it easy to run and manage AppImages.
        
        1. Install AppImageLauncher:
              ```sh
          paru appimagelauncher
              ```
        2. Download an Appimage of your choice from a trusted source.

        3. Double click the downloaded AppImage file. AppImageLauncher will prompt you to integrate the application into your system.

        4. Follow the prompts to complete the integration process.

        5. Once integrated, you can launch the application from your application menu or by double clicking the AppImage file.
        
    

## Configuring Access to Samba Shares

Samba is a free software re-implementation of the SMB networking protocol. To connect to your samba server, a useful config has been made available to CachyOS users, but it requires changing the configuration of your samba server.

### Installing and using the CachyOS smb.conf file

To use the convenient smb.conf file, first install a specific package that provides the required smb.conf file. Then, replace your server's existing smb.conf with this file and reconfigure your shared volumes.

> **Note – This guide assumes you already have a working Samba server:**

    1. Create a backup of your original `smb.conf` file, typically located at `/etc/samba/smb.conf` on Linux systems.
    2. Install the CachyOS Samba settings package on your client machine:
        ```sh
    sudo pacman -S cachyos-samba-settings
        ```
    3. Copy the `smb.conf` from your client machine to the Samba server.
    4. Open and edit the file to add your shared directories, printers, etc.
    5. Restart the Samba service on your server:
        ```sh
    sudo systemctl restart --now samba
        ```
    6. On the client machine, access your shared resources through your file manager (e.g., `smb://&lt;your_server_ip&gt;/&lt;share_name&gt;`).

        If configured correctly, you'll be prompted for login credentials. Remember to select the option to save your login information if desired.

<a id="configuration-sched-ext"></a>
#### sched-ext Tutorial

Extensible Scheduler Class (better known as `sched-ext`) is a Linux kernel feature which enables implementing kernel thread schedulers in
BPF (Berkeley Package Filter) and dynamically loading them. Essentially, this allows end-users to change their schedulers in userspace without
the need to build another kernel just to have a different scheduler.

> **Tip – Get in touch with the developers on their [Discord server:**

- *The schedulers can be found in the `scx-scheds` and `scx-scheds-git` package.*
  ```sh
  # Stable branch + scx_loader and scxctl tools.
  sudo pacman -S scx-scheds scx-tools

  # Bleeding edge branch (This branch includes the latest changes from the master branch.) + scx_loader and scxctl tools.
  sudo pacman -S scx-scheds-git scx-tools-git
  ```

> **Note:**
> The `scx-scheds-git` package may not include every experimental scheduler, as some are developed in separate feature branches that are not yet merged into the master branch.

<a id="configuration-sched-ext-how-to-launch-and-manage-the-scheduler"></a>
### How to Launch and Manage the Scheduler

<a id="configuration-sched-ext-terminal"></a>
###### Terminal

- *To start the scheduler, open your terminal and enter the following command:*
  ```sh title='Example of starting rusty'
  sudo scx_rusty
  ```

*This will launch the rusty scheduler and detach the default scheduler.*

To stop the scheduler. Press `CTRL + C` and the scheduler will then be stopped and the default kernel scheduler will take over again.

<a id="configuration-sched-ext-scxctl"></a>
###### scxctl

> **Note – Included in the `scx-scheds` and `scx-scheds-git` package:**

`scxctl` is a CLI DBUS client for interacting with `scx_loader`.

Since it does **not require sudo privileges**, you can manage schedulers as a regular user.

This opens up possibilities for creative setups: for example, you could create keybindings or scripts to switch profiles, execute schedulers in specific modes, or automate tasks all without needing root access.

- Features:
- Get the current scheduler and mode
- List all available schedulers
- Start a scheduler in a given mode, or with given arguments
- Switch between schedulers and modes
- Stop the running scheduler
- Restart the running scheduler

<a id="configuration-sched-ext-starting-a-scheduler"></a>
###### Starting a scheduler

          ```sh title='Starting scx_flash in Gaming mode'
          scxctl start --sched flash --mode gaming
          ```

<a id="configuration-sched-ext-stopping-a-scheduler"></a>
###### Stopping a scheduler

          ```sh title='Stopping the currently running scheduler'
          scxctl stop
          ```

<a id="configuration-sched-ext-switching-schedulers"></a>
###### Switching schedulers

          ```sh title='Switching to scx_bpfland in Gaming mode'
          scxctl switch --sched bpfland --mode gaming
          ```

<a id="configuration-sched-ext-starting-switching-with-custom-arguments"></a>
###### Starting & Switching with custom arguments

> **Note – Add a comma between each argument:**
> Example: `--args="-c,75,-m,0-15"` = Argument, Value
          ```sh title='Starting scx_cosmos with custom arguments'
          scxctl start --sched cosmos --args="-c,75,-m,0-15"
          ```
          ```sh title='Switching to scx_flash with custom arguments'
          scxctl switch --sched flash --args="-s,20000"
          ```

```sh
$ scxctl --help
Usage: scxctl &lt;COMMAND&gt;

Commands:
  get     Get the current scheduler and mode
  list    List all supported schedulers
  start   Start a scheduler in a mode or with arguments
  switch  Switch schedulers or modes, optionally with arguments
  stop    Stop the current scheduler
  restart Restart the current scheduler with original configuration
  help    Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version
```

<a id="configuration-sched-ext-scxloader-dbus"></a>
###### scx_loader (DBus)

*As the name implies, it is a utility that functions as a loader and manager for the sched-ext framework using the D-Bus interface.*

*While it does not require systemd, it can still be utilized in conjunction with it.* [Check the transition guide for reference](#configuration-sched-ext-transitioning-from-scxservice-to-scxloader-a-comprehensive-guide).

- Has the ability to stop, start, restart, read information about a scx scheduler and more.
- *You can use tools like `dbus-send` or `gdbus` to communicate with it.*
- This guide explains how to use scx_loader with the dbus-send command.
- ```sh title='Starting scx_rusty with its default arguments'
dbus-send --system --print-reply --dest=org.scx.Loader /org/scx/Loader org.scx.Loader.StartScheduler string:scx_rusty uint32:0
    ```
  - ```sh title='Starting a scheduler with arguments'
    # This example starts scx_bpfland with the following flags: -k -c 0
    dbus-send --system --print-reply --dest=org.scx.Loader /org/scx/Loader org.scx.Loader.StartSchedulerWithArgs string:scx_bpfland array:string:"-k","-c","0"
    ```
- ```sh title='Stopping the currently running scheduler'
dbus-send --system --print-reply --dest=org.scx.Loader /org/scx/Loader org.scx.Loader.StopScheduler
    ```
  - ```sh title='Switching to another scheduler in Mode 2'
    dbus-send --system --print-reply --dest=org.scx.Loader /org/scx/Loader org.scx.Loader.SwitchScheduler string:scx_lavd uint32:2
    # This switches to scx_lavd with the scheduler mode 2 meaning it starts LAVD in powersaving
    ```
- ```sh title='Switching to another scheduler with arguments'
dbus-send --system --print-reply --dest=org.scx.Loader /org/scx/Loader org.scx.Loader.SwitchSchedulerWithArgs string:scx_bpfland array:string:"-k","-c","0"
    ```
  - ```sh title='Getting the currently running scheduler'
    dbus-send --system --print-reply --dest=org.scx.Loader /org/scx/Loader org.freedesktop.DBus.Properties.Get string:org.scx.Loader string:CurrentScheduler
    ```
- ```sh title='Getting a list of the supported schedulers'
dbus-send --system --print-reply --dest=org.scx.Loader /org/scx/Loader org.freedesktop.DBus.Properties.Get string:org.scx.Loader string:SupportedSchedulers
    ```
> **Tip:**
> Here is an explanation of what each mode means in scx_loader:
>
> - Mode 0 = `Default scheduler flags`
> - Mode 1 = `Gaming`
> - Mode 2 = `Power Saving`
> - Mode 3 = `Low Latency`
> - Mode 4 = `Server`
>
> Example: LAVD running in Mode 1 is the equivalent of `scx_lavd --performance`
>
> *TLDR: Each mode is a set of different flags meant to improve the intended use case.*
>
> [For a more in depth look on what these Modes change on each scheduler](<https://github.com/sched-ext/scx/blob/main/tools/scx_loader/src/config.rs#L174>)

##### CachyOS Kernel Manager

You can access and configure them via the `sched-ext scheduler config` button.

##### SCX Manager

SCX Manager is a standalone GUI tool derived from the CachyOS Kernel Manager. It allows users to manage the sched-ext framework and its schedulers through the `scx_loader`.

Features:
- Check which scheduler is currently active
- Select a scheduler or profile: (Auto, Gaming, Power save, Low Latency or Server)
- Set additional flags
- Disable the current scheduler

**Screenshot:**

![Image](src/assets/images/scx-manager-main.png)

## Scheduler Guide: Profiles and Use Cases

Since there are many schedulers to choose from, we want to give a little introduction about the schedulers in hand.

> **Note:**
> These schedulers are in constant development while being tested, so expect some of its features/flags which are subject to change.

Feel free to report any issue or feedback to their scheduler repository.

Use `scx_schedulername --help` to see the available flags and a brief description of what they do.

```sh title='Example of getting help for scx_rusty'
scx_rusty --help
```

### [scx_bpfland](<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_bpfland>)

**Developed by: Andrea Righi (arighi [GitHub](<https://github.com/arighi>))**

Production Ready? ✅

A vruntime-based sched_ext scheduler that prioritizes interactive workloads. Highly flexible and easy to adapt.

Bpfland when making decisions on which cores to use, it takes in consideration their cache layout and which cores share the same L2/L3 cache leading to fewer cache misses = more performance.

- Use cases:
  - Gaming
  - Desktop usage
  - Multimedia/Audio production
  - Great interactivity under intensive workloads
  - Power saving
  - Server

#### Scheduler Modes

##### Low Latency

* **Command-line Flags:** `-s 5000 -S 500 -l 5000 -m performance`
* **Description:** Meant to lower latency at the cost of throughput. Suitable for soft real-time applications like Audio Processing and Multimedia.

##### Power Save

* **Command-line Flags:** `-m powersave`
* **Description:** Prioritizes power efficiency. Favors less performant cores (e.g E-cores on Intel).

##### Server

* **Command-line Flags:** `-p`
* **Description:** Prioritize tasks with strict affinity. This option can increase throughput at the cost of latency and it is more suitable for server workloads.

### [scx_beerland](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_beerland)

**Developed by: Andrea Righi (arighi [GitHub](<https://github.com/arighi>))**

Production Ready? ✅

scx_beerland is a scheduler designed to prioritize locality and scalability.

Prioritizes keeping tasks on the same CPU to maintain cache locality, while also ensuring good scalability across many CPUs by using local DSQs (per-CPU runqueues) when the system is not saturated.

- Use cases:
  - Cache-intensive workloads
  - Systems with a large amount of CPUs
  - Gaming: Its known to work surprinsingly well in certain games, although your mileage may vary
  - Server: Good for general purpose server workloads due to its scalability and locality optimizations.
  - Can be used for desktop usage as well.

#### Scheduler Modes

None for the moment.

### [scx_rustland](<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_rustland>)

**Developed by: Andrea Righi (arighi [GitHub](<https://github.com/arighi>))**

Production Ready? 

For performance-critical production scenarios, other schedulers are likely to exhibit better performance, as offloading all scheduling decisions to user-space comes with a certain cost (even if it's minimal).

However, a scheduler entirely implemented in user-space holds the potential for seamless integration with sophisticated libraries, tracing tools, external services (e.g., AI), etc.

Hence, there might be situations where the benefits outweigh the overhead, justifying the use of this scheduler in a production environment.

Shares similarities with bpfland, Made with the intention of being easy to read and understand how it works due to its implementation in userspace.

Keep in mind that there is a slight throughput disadvantage when using a userspace scheduler.

- Use cases:
  - Low latency workloads (Gaming, video conferences and live streaming)
  - Desktop usage

### [scx_flash](<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_flash>)

**Developed by: Andrea Righi (arighi [GitHub](<https://github.com/arighi>))**

Production Ready? ✅

A scheduler that focuses on ensuring fairness among tasks and performance predictability.

It operates using an [earliest deadline first (EDF) policy](https://www.geeksforgeeks.org/operating-systems/earliest-deadline-first-edf-cpu-scheduling-algorithm/), where each task is assigned a "latency" weight. This weight is dynamically adjusted based on how often a task release the CPU before its full time slice is used.

Tasks that release the CPU early are given a higher latency weight, prioritizing them over tasks that fully consume their time slice.

- Use cases:
  - Gaming
  - Latency sensitive workloads such as multimedia or real-time audio processing
  - Need for responsiveness under over-stressed situations
  - Consistency in performance
  - Server

#### Scheduler Modes

##### Low Latency

* **Command-line Flags:** `-m performance -w -C 0`
* **Description:** Meant to lower latency at the cost of throughput. Suitable for soft real-time applications like Audio Processing and Multimedia.

##### Gaming

* **Command-line Flags:** `-m all`
* **Description:** Optimizes for high performance in games.

##### Power Save

* **Command-line Flags:** `-m powersave -I 10000 -t 10000 -s 10000 -S 1000`
* **Description:** Prioritizes power efficiency. Favor less performant cores (e.g., E-cores on Intel) and introduces a forced idle cycle every 10ms to increase power saving.

##### Server

* **Command-line Flags:** `-m all -s 20000 -S 1000 -I -1 -D -L`
* **Description:** Tuned for server workloads. Trades responsiveness for throughput.

### [scx_cosmos](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_cosmos)

**Developed by: Andrea Righi (arighi [GitHub](<https://github.com/arighi>))**

- Production Ready? ✅

Lightweight scheduler optimized for preserving task-to-CPU locality.

When the system is not saturated, the scheduler prioritizes keeping tasks on the same CPU using local DSQs. This not only maintains locality but also reduces locking contention compared to shared DSQs, enabling good scalability across many CPUs.

- Use cases:
  - General-purpose scheduler: the scheduler should adapt itself both for server workloads or desktop workloads.

#### Scheduler Modes

##### Auto

* **Command-line Flags:** `-d`
* **Description:** Disables deferred wakeups. Reduces throughput and performance for certain workloads while decreasing power consumption.

##### Gaming

* **Command-line Flags:** `-c 0 -p 0`
* **Description:** Disable CPU load tracking and always enforce deadline-based scheduling to improve responsiveness.

##### Power Save

* **Command-line Flags:** `-m powersave -d -p 5000`
* **Description:** Prioritizes power efficiency. Favor less performant cores (e.g., E-cores on Intel) and disables deferred wakeups, reducing throughput while increasing power efficiency. CPU load polling increased to 5ms.

##### Low Latency

* **Command-line Flags:** `-m performance -c 0 -p 0 -w`
* **Description:** Meant to lower latency at the cost of throughput. Suitable for soft real-time applications like Audio Processing and Multimedia. Always enforce deadline-based scheduling and synchronous wake up optimizations to improve performance predictability.

##### Server

* **Command-line Flags:** `-a -s 20000`
* **Description:** Enable address space affinity to improve locality and performance in certain cache-sensitive workloads. Polling increased to 20ms.

### [scx_lavd](<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_lavd>)

**Developed by: Changwoo Min (multics69 [GitHub](<https://github.com/multics69>)).**

- Production Ready? ✅

Brief introduction to LAVD from Changwoo:

*LAVD is a new scheduling algorithm which is still under development. It is
motivated by gaming workloads, which are latency-critical and
communication-heavy. It aims to minimize latency spikes while maintaining
overall good throughput and fair use of CPU time among tasks.*

- Use cases:
  - Gaming
  - Audio Production
  - Latency sensitive workloads
  - Desktop usage
  - Great interactivity under intensive workloads
  - Power saving

One of the main and awesome capabilities that LAVD includes is **Core Compaction.** which without going into technical details: When CPU usage < 50%, Currently active cores will run for longer and at a higher frequency. Meanwhile Idle Cores will stay in C-State (Sleep) for a much longer duration achieving less overall power usage.

##### Scheduler Modes

##### Gaming & Low Latency

* **Command-line Flags:** `--performance`
* **Description:** Maximizes performance by using all available cores, prioritizing physical cores.

##### Power Save

* **Command-line Flags:** `--powersave`
* **Description:** Minimizes power consumption while maintaining reasonable performance. Prioritizes efficient cores and threads over physical cores.

### [scx_rusty](<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_rusty>)

**Developed by: David Vernet (Byte-Lab [GitHub](<https://github.com/Byte-Lab>))**

- Production Ready? 
  - Yes. If tuned correctly,

Rusty offers a wide range of features that enhance its capabilities, providing greater flexibility for various use cases.
One of these features is tunability, allowing you to customize Rusty to suit your preferences and specific requirements.

- Use cases:
  - Gaming
  - Latency sensitive workloads
  - Desktop usage
  - Multimedia/Audio production
  - Great interactivity under intensive workloads
  - Power saving

### [scx_p2dq](<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_p2dq>)

- Production Ready? 
  - Yes. If tuned correctly for your specific workload and hardware.

**Developed by: Daniel Hodges (hodgesds [GitHub](<https://github.com/hodgesds>))**

A general purpose scheduler that focuses on pick two load balancing between
LLCs. Keeps high cache locality and work conservation while providing
reasonable latency.

- Use cases:
  - Server
  - Desktop environments
  - Gaming (with some manual tuning)

#### Scheduler Modes

##### Gaming

* **Command-line Flags:** `--task-slice true -f --sched-mode performance`
* **Description:** Improves consistency in gaming performance and increases bias towards scheduling on higher performance cores.

##### Low Latency

* **Command-line Flags:** `-y -f --task-slice true`
* **Description:** Lowers latency by making interactive tasks stick more to the CPU they were assigned to and increasing the stability on slice time.

##### Power Save

* **Command-line Flags:** `--sched-mode efficiency`
* **Description:** Enhances power efficiency by prioritizing power efficient cores.

##### Server

* **Command-line Flags:** `--keep-running`
* **Description:** Improves server workloads by allowing tasks to run beyond their slice if the CPU is idle.

### [scx_tickless](<https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_tickless>)

**Developed by: Andrea Righi (arighi [Github](<https://github.com/arighi>))**

- Production Ready? 
  - This scheduler is still experimental and not recommended for production use.

> **Note:**
> In order to effectively disable ticks on the "tickless" CPUs the kernel must be booted with `nohz_full`. Keep in mind that `nohz_full` introduces syscall overhead, so this may regress latency-sensitive workloads.

scx_tickless is a server-oriented scheduler designed for cloud computing, virtualization, and high-performance computing workloads.

The scheduler works by routing all scheduling events through a pool of primary CPUs assigned to handle these events. This allows disabling the scheduler's tick on other CPUs, reducing OS noise.

- Use cases:
  - Cloud computing
  - Virtualization
  - High performance computing workloads
  - Server

#### Scheduler Modes

##### Gaming

* **Command-line Flags:** `-f 5000 -s 5000`
* **Description:** Boosts gaming performance by increasing how often the scheduler detects CPU contention and triggers context switches with a shorter time slice.

##### Power Save

* **Command-line Flags:** `-f 50 -p`
* **Description:** Enhances power efficiency by lowering contention checks and aggressively trying to keep tasks on the same CPU.

##### Low Latency
* **Command-line Flags:** `-f 5000 -s 1000`
* **Description:** Similar to the gaming profile but with a further reduced slice.

##### Server

* **Command-line Flags:** `-f 100`
* **Description:** Reduced how often the scheduler checks for CPU contention to improve throughput at the cost of responsiveness.

## Configuration and performance testing

### LAVD Autopilot & Autopower

*Quotes from Changwoo Min:*
- In autopilot mode, the scheduler adjusts its power mode `Powersave, Balanced, or Performance` based on the system load, specifically CPU utilization

- Autopower: Automatically decide the scheduler's power mode based on the system's energy profile aka EPP (Energy Performance Preference).

```sh
<a id="configuration-sched-ext-autopower-can-be-activated-by-the-following-flag"></a>
## Autopower can be activated by the following flag:
--autopower
<a id="configuration-sched-ext-eg"></a>
## e.g:
scx_lavd --autopower
```

### ananicy-cpp & sched-ext

> **Note – Update about ananicy-cpp and sched-ext:**
> After further development of the schedulers, ananicy-cpp is usually okay to be used alongside them. However, if you experience any stalls or instability, consider disabling it as a troubleshooting step.

In order to disable/stop ananicy-cpp, run the following command:

```sh
systemctl disable --now ananicy-cpp
```

### Benchmarking and comparing schedulers with cachyos-benchmarker

The [cachyos-benchmarker](https://github.com/CachyOS/cachyos-benchmarker) tool provides an easy way to evaluate and compare the performance of different CPU schedulers.

It runs a comprehensive suite of benchmarks to measure CPU, memory, and overall system performance under various workloads.

The following benchmarks are included:

| Test                        | Measures                                 | Tool         |
| --------------------------- | ---------------------------------------- | ------------ |
| **stress-ng cpu-cache-mem** | CPU, cache, and memory performance       | `stress-ng`  |
| **FFmpeg compilation**      | Parallel build performance               | `make`       |
| **x265 encoding**           | Video encoding throughput                | `x265`       |
| **argon2 hashing**          | Multithreaded password hashing           | `argon2`     |
| **perf sched msg**          | Context switching and IPC performance    | `perf`       |
| **perf memcpy**             | Memory throughput `memcpy()`             | `perf`       |
| **prime calculation**       | Integer arithmetic and parallelism       | `primesieve` |
| **NAMD**                    | Molecular dynamics (scientific workload) | `namd3`      |
| **Blender render**          | CPU-only 3D rendering                    | `blender`    |
| **xz compression**          | Compression throughput                   | `xz`         |
| **Kernel defconfig build**  | Kernel compilation performance           | `make`       |
| **y-cruncher**              | Mathematical precision and memory stress | `y-cruncher` |

`cachyos-benchmarker` can be used for several purposes, including:

- **Testing scheduler stability**
  Run the full benchmark suite to detect stalls, crashes, or regressions introduced by scheduler changes.
  If you are using `scx_loader`, you can collect logs in case of a stall or crash with:
  ```bash
  journalctl --unit scx_loader.service --boot 0 > crash.log
  ```
  This will create a file named `crash.log` in your current directory.
- **Comparing scheduler performance**
  - Evaluate performance differences between schedulers. e.G. `BPFLAND vs LAVD`
- **Measuring the effect of kernel or scheduler updates**
  - Compare runs before and after applying patches or version changes to check for performance regressions or improvements.
- **Testing configuration tweaks**
  - Assess the impact of changes such as CPU governor settings, SMT toggling, or modified scheduler flags.

#### Requirements
- 4 GB RAM or more
- At least 8 GB of free storage space
- Time and patience - **the full benchmark can take over an hour on slower systems**

#### Installation

To install `cachyos-benchmarker`, run the following command:
```bash
sudo pacman -S cachyos-benchmarker
```

#### Running the benchmark

    1. Execute `cachyos-benchmarker:`
        ```bash
    cachyos-benchmarker ~/cachyos-benchmarker/
<a id="configuration-sched-ext-you-can-replace-cachyos-benchmarker-with-any-directory-you-want-the-logs-to-be-saved-in"></a>
## You can replace ~/cachyos-benchmarker/ with any directory you want the logs to be saved in.
        ```
    2. Wait until the preparation steps finish.
    3. Follow the prompts:
        - `Do you want to drop page cache now? Root privileges needed! (y/N) y`
        - `Please enter a name for this run, or leave empty for default:`
    4. Wait for the tests to finish.
    5. Once finished, the following will happen:
        - Creation of a log file with name like `benchie_&lt;name&gt;_&lt;DATE&gt;.log` which contains detailed information about the benchmark run.
          - Example: `benchie_p2dq_2025-09-29-2115.log`
          - The `benchmark_scraper.py` script will automatically execute to generate a summary report in HTML format.
          - What does the script do?:
            - Reads all `benchie_*.log` files in the specified directory.
            - Extracts the benchmark names, times, and scores.
            - Sorts or aggregates them.
            - Prints a clean summary of the results to your terminal and creates an HTML file that can be opened in a browser.
                
                **Terminal output example::**
                ```text
            stress-ng cpu-cache-mem: 15.26
            y-cruncher pi 1b: 31.23
            perf sched msg fork thread: 8.892
            perf memcpy: 13.53
            namd 92K atoms: 53.54
            calculating prime numbers: 11.126
            argon2 hashing: 6.62
            ffmpeg compilation: 53.38
            xz compression: 61.13
            kernel defconfig: 130.73
            blender render: 96.29
            x265 encoding: 24.99

            Total time (s): 506.72
            Total score: 70.71

            Name: p2dq
            Date: 2025-09-29-2115

            System:    Kernel: 6.17.0-1.1-cachyos-p2dq arch: x86_64 bits: 64
                       Desktop: KDE Plasma v: 6.4.5 Distro: CachyOS
            Memory:    System RAM: total: 32 GiB available: 30.61 GiB used: 7.54 GiB (24.6%)
                       Device-1: Channel-A DIMM 0 type: LPDDR5 size: 8 GiB speed: 7500 MT/s
                       Device-2: Channel-B DIMM 0 type: LPDDR5 size: 8 GiB speed: 7500 MT/s
                       Device-3: Channel-C DIMM 0 type: LPDDR5 size: 8 GiB speed: 7500 MT/s
                       Device-4: Channel-D DIMM 0 type: LPDDR5 size: 8 GiB speed: 7500 MT/s
            CPU:       Info: 8-core model: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics bits: 64 type: MT MCP cache: L2: 8 MiB
                       Speed (MHz): avg: 3366 min/max: 419/5138 cores: 1: 3366 2: 3366 3: 3366 4: 3366 5: 3366 6: 3366 7: 3366 8: 3366 9: 3366 10: 3366 11: 3366 12: 3366 13: 3366 14: 3366 15: 3366 16: 3366

            SCX Scheduler: p2dq_1.0.21_gf90c2aa1_dirty_x86_64_unknown_linux_gnu

            SCX Version: p2dq_1.0.21_gf90c2aa1_dirty_x86_64_unknown_linux_gnu

             Version         : 0.5.1-1
                ```
                
                
                **HTML example of a test result comparing two different branches of the same scheduler::**
                ![Image](src/assets/images/cachyos-benchmarker-example.png)
                
    6. To compare two or more runs, place the `.log` files in the same directory before running `benchmark_scraper.py`. The tool will automatically detect and compare them in the HTML report.

### Testing scheduler latency with schbench

schbench is a scheduler benchmark designed to measure scheduler latency under a simulated server-style workload. It spawns a configurable number of "worker" and "message" threads, where messages repeatedly wake up workers. By measuring the latency distribution from wakeup to execution of these worker threads, it provides critical insight into a kernel's ability to handle thread wakeups, balancing, and CPU contention, especially under load.

#### Use cases

You can use `schbench` to:

- **Evaluate scheduler latency:** Identify how quickly threads are scheduled after waking up.
- **Compare wakeup performance between schedulers:** Detect improvements or regressions in context switching and wakeup latency.
- **Test the effect of kernel or scheduler patches:** Assess if tuning or updates affect scheduling fairness and responsiveness.

#### Installation

`schbench` is available in the CachyOS repositories:
```bash
sudo pacman -S schbench
```

#### Running the benchmark

A simple way to run `schbench`for a general latency test is:
```bash
schbench -m 2 -t 8 -r 60
```

This example runs:
- 2 message threads (`-m 2`)
- 8 worker threads per message thread (`-t 8`)
- for 60 seconds total runtime (`-r 60`)

You can adjust these values depending on your CPU core count and the desired load level.

Here is a table explaining some of the key options:

| Option                       | Description                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| `-C, --calibrate`            | Run calibration and report timing (no benchmark).               |
| `-L, --no-locking`           | Disable spinlocks during CPU work (default: locking enabled).   |
| `-m, --message-threads &lt;n&gt;`  | Number of message threads (default: 1).                         |
| `-t, --threads &lt;n&gt;`          | Worker threads per message thread (default: number of CPUs).    |
| `-r, --runtime &lt;sec&gt;`        | Benchmark duration (default: 30).                               |
| `-F, --cache_footprint &lt;KB&gt;` | Cache footprint size (default: 256).                            |
| `-n, --operations &lt;count&gt;`   | Number of "think time" operations to perform (default: 5).      |
| `-A, --auto-rps`             | Automatically grow RPS until CPU utilization target is reached. |
| `-R, --rps &lt;count&gt;`          | Requests per second mode.                                       |
| `-p, --pipe &lt;bytes&gt;`         | Simulate a pipe transfer test.                                  |
| `-w, --warmuptime &lt;sec&gt;`     | Warm-up duration before collecting stats (default: 0).          |
| `-i, --intervaltime &lt;sec&gt;`   | Interval for printing latencies (default: 10).                  |
| `-z, --zerotime &lt;sec&gt;`       | Interval for zeroing latency stats (default: never).            |

#### Understanding the output

After each run, `schbench` prints latency percentiles like:

    **Output example:**
    ```bash
Wakeup Latencies percentiles (usec) runtime 10 (s) (2406 total samples)
	  50.0th: 60         (648 samples)
	  90.0th: 2034       (968 samples)
	* 99.0th: 4104       (211 samples)
	  99.9th: 10128      (22 samples)
	  min=1, max=10308
Request Latencies percentiles (usec) runtime 10 (s) (2394 total samples)
	  50.0th: 49216      (726 samples)
	  90.0th: 69760      (954 samples)
	* 99.0th: 166656     (212 samples)
	  99.9th: 273920     (21 samples)
	  min=11770, max=334247
RPS percentiles (requests) runtime 10 (s) (11 total samples)
	  20.0th: 234        (3 samples)
	* 50.0th: 238        (3 samples)
	  90.0th: 241        (4 samples)
	  min=230, max=248
current rps: 230.99
Wakeup Latencies percentiles (usec) runtime 10 (s) (2406 total samples)
	  50.0th: 60         (648 samples)
	  90.0th: 2034       (968 samples)
	* 99.0th: 4104       (211 samples)
	  99.9th: 10128      (22 samples)
	  min=1, max=10308
Request Latencies percentiles (usec) runtime 10 (s) (2406 total samples)
	  50.0th: 49216      (729 samples)
	  90.0th: 69760      (956 samples)
	* 99.0th: 165632     (212 samples)
	  99.9th: 273920     (22 samples)
	  min=11770, max=334247
RPS percentiles (requests) runtime 10 (s) (11 total samples)
	  20.0th: 234        (3 samples)
	* 50.0th: 238        (3 samples)
	  90.0th: 241        (4 samples)
	  min=230, max=248
average rps: 240.60
    ```

##### How to interpret the results

- **Wakeup Latencies:**
  - Measures how quickly threads wake up after being signaled.
    - Lower values here (especially the **99th percentile**) mean the scheduler is more responsive.
- **Request Latencies:**
  - Represents the time taken to complete requests between threads.
    - Lower latency indicates better inter-thread communication and scheduling efficiency.
- **RPS (Requests Per Second):**
  - Shows the sustained throughput:
    - A higher **average RPS** indicates the scheduler can handle more work per second under the given configuration.

In conclusion:
- A **good scheduler** will show **low wakeup and request latencies** with **consistent RPS**.
- A **less efficient scheduler** may exhibit **high latency spikes** or **unstable RPS values** over time.

> **Note:**
> These results can vary based on the CPU, core count, system load and if the scheduler is capable of handling your CPU architecture efficiently.

### Recommendations for benchmarking games

If your desire is to benchmark games to compare how different schedulers perform, here are some tips to get the most accurate results:

- **Use built-in benchmarks:** Many modern games come with built-in benchmarking tools. These are designed to provide consistent results by running the same sequence of events each time.
  - Check out this [website](https://www.pcgamingwiki.com/wiki/List_of_games_with_built-in_benchmarks) for a list of games that include built-in benchmarks.
- **Consistent settings:** Ensure that the game settings (resolution, graphics quality, etc.) are the same for each test run.
- **Close background applications:** Other applications running in the background can affect performance. Close unnecessary programs to minimize their impact.
- If you're not using a built-in benchmark, try to perform the same actions in the game for each test run. This could include following the same path, engaging in similar combat scenarios, or performing the same tasks.
  - Even not aiming at the same spot can lead to different performance results.
- **Multiple runs:** Perform multiple runs of the benchmark and take the average to account for variability.
- **Use performance monitoring tools:** Tools like MangoHud or GOverlay can provide realtime performance metrics such as FPS, frame times, and CPU/GPU usage.
- **Take advantage of keyboard shortcuts or macros:**
  - One example is to create a keybinding on which you can switch between different schedulers or change their modes on the fly while in-game.
    - This can be done using a tool like [scxctl](#configuration-sched-ext-how-to-launch-and-manage-the-scheduler) or by creating custom scripts that change the active scheduler and its mode.

#### Uploading and sharing your benchmarks

This [website](https://flightlesssomething.ambrosia.one/benchmarks) contains a list of benchmarks done by the community using different schedulers or testing various settings.

In order to upload your own benchmarks. You'll have to link your Discord account to the website and then you can submit your own benchmarks.

Then click on the `New benchmark` button and fill in the required information.

- You can upload multiple results for the same game using different schedulers or settings.
- Accepts both MangoHud and Afterburner logs.
- Allows searching by title or description.

## Transitioning from scx.service to scx_loader: A Comprehensive Guide

> **Caution:**
> Do not attempt to run the scx_loader.service alongside the scx.service otherwise, the loader service will start but do nothing.
>
> This conflict arises because both services are unaware of each other, especially regarding which one manages the schedulers.

> **Tip:**
> The CachyOS Kernel Manager already includes a [GUI for managing the scx_loader.](#features-kernel-manager-sched-ext-framework-management)

First let's start with a close-up comparison between the scx.service file structure against the scx_loader configuration file structure.

*If you previously had LAVD running with the old scx.service like this example below:*

```sh title='scx.service file structure'
<a id="configuration-sched-ext-list-of-scxschedulers-scxbpfland-scxcentral-scxflash-scxlavd-scxlayered-scxnest-scxqmap-scxrlfifo-scxrustland-scxrusty-scxsimple-scxuserland"></a>
## List of scx_schedulers: scx_bpfland scx_central scx_flash scx_lavd scx_layered scx_nest scx_qmap scx_rlfifo scx_rustland scx_rusty scx_simple scx_userland
SCX_SCHEDULER=scx_lavd

<a id="configuration-sched-ext-set-custom-flags-for-the-scheduler"></a>
## Set custom flags for the scheduler
SCX_FLAGS='--performance'
```

Then the equivalent on the scx_loader configuration file will look like:

```sh title='scx_loader file structure'
default_sched = "scx_lavd"
default_mode = "Auto"

[scheds.scx_lavd]
auto_mode = ["--performance"]
```

[For more information on how to configure the scx_loader file](https://github.com/sched-ext/scx-loader/blob/main/crates/scx_loader/configuration.md#scx_loader-configuration-file)

  Follow the guide below for an easy transition from the `scx systemd service` to the new `scx_loader` utility.
  
  1. ```sh title='Disabling scx.service in favor of the scx_loader.service'
      systemctl disable --now scx.service && systemctl enable --now scx_loader.service
      ```
  2. ```sh title='Creating the configuration file for the scx_loader and adding the default structure'
<a id="configuration-sched-ext-micro-editor-is-going-to-create-a-new-file"></a>
## Micro editor is going to create a new file.
 sudo micro /etc/scx_loader.toml
<a id="configuration-sched-ext-add-the-following-lines"></a>
## Add the following lines:

 default_sched = "scx_bpfland" # Edit this line to the scheduler you want scx_loader to start at boot
 default_mode = "Auto" # Possible values: "Auto", "Gaming", "LowLatency", "PowerSave".

<a id="configuration-sched-ext-press-ctrl-s-to-save-changes-and-ctrl-q-to-exit-micro"></a>
## Press CTRL + S to save changes and CTRL + Q to exit Micro.
     ```
  3. ```sh title='Restarting the scx_loader'
     systemctl restart scx_loader.service
     ```
 - You're done, the scx_loader will now load and start the desired scheduler.

  

<a id="configuration-sched-ext-debugging-in-the-scxloader"></a>
#### Debugging in the scx_loader

<a id="configuration-sched-ext-simple-logging"></a>
###### Simple logging

- ```sh title='Checking the service status'
systemctl status scx_loader.service
    ```
  - ```sh title='Viewing all the service log entries'
    journalctl -u scx_loader.service
    ```
- ```sh title='Viewing only the logs of the current session.'
journalctl -u scx_loader.service -b 0
    ```

##### Extended logging

*In order to get a more detailed log, follow these steps.*
  - ```sh title='Edit the service file'
     sudo systemctl edit scx_loader.service
     ```
- ```sh title='Add the following line under the [Service] section'
 Environment=RUST_LOG=trace
     ```
  - ```sh title='Restart the service'
     sudo systemctl restart scx_loader.service
     ```
- Check the logs again for a more detailed debugging information.

<a id="configuration-sched-ext-faq"></a>
### FAQ

<a id="configuration-sched-ext-why-x-scheduler-performs-worse-than-the-other"></a>
#### Why X scheduler performs worse than the other?

- There are many variables to consider when comparing them. For example, how do they measure a task's weight? Do they prioritize interactive tasks over non-interactive ones?
  Ultimately, it depends on their design choices.

<a id="configuration-sched-ext-why-everyone-keeps-saying-this-x-scheduler-is-the-best-for-x-case-but-it-does-not-perform-as-well-for-me"></a>
#### Why everyone keeps saying this X scheduler is the best for X case but it does not perform as well for me?

- Like the previous answer, the choice of CPU and its design such as the core layout, how they share cache across the cores and other related factors can lead to the scheduler operating less efficiently.
- That's why having choices is one of the highlights from the sched-ext framework, so don't be scared to try one and see which one works best for your use case. `Examples: fps stability, maximum performance, responsiveness under intensive workloads etc.`

<a id="configuration-sched-ext-the-use-cases-of-these-schedulers-are-quite-similar-why-is-that"></a>
#### The use cases of these schedulers are quite similar... why is that?

Primarily because they are multipurpose schedulers, which means they can accommodate a variety of workloads, even if they may not excel in every area.

- To determine which scheduler suits you best, there's no better advice than to try it out for yourself.

<a id="configuration-sched-ext-why-am-i-missing-a-scheduler-that-some-users-are-mentioning-or-testing-in-the-cachyos-discord-server"></a>
#### Why am I missing a scheduler that some users are mentioning or testing in the CachyOS Discord server?
Make sure you're using the bleeding edge version of the scx-scheds package named as `scx-scheds-git`

- One of the reasons will be that this scheduler is very new and is currently being tested by the users, therefore it has not yet been added to the `scx-scheds-git` package.

<a id="configuration-sched-ext-why-did-the-scheduler-suddenly-crash-is-it-unstable"></a>
#### Why did the scheduler suddenly crash? Is it unstable?

- *There could be a few reasons on why this happened:*
- One of the most common reason is that you were using ananicy-cpp alongside the scheduler. This why we added this [warning](#configuration-sched-ext-disable-ananicy-cpp)
- Another reason could be that the workload you were running exceeded the limits and capacity of the scheduler causing it to stall.
- Example of an unreasonable workload: `hackbench`
- Or the more obvious reason, you've found a bug in the scheduler, if so. Please report it as an issue in their [GitHub](https://github.com/sched-ext/scx/issues) or let them know
about it in the CachyOS Discord channel `sched-ext`

<a id="configuration-sched-ext-i-have-previously-used-the-scxloader-in-the-kernel-manager-gui-do-i-still-need-to-follow-the-transition-steps"></a>
#### I have previously used the scx_loader in the Kernel Manager GUI. Do I still need to follow the transition steps?

- In this particular case, no, it is not necessary because the Kernel Manager already handles the transition process.
- *Unless you have previously added custom flags in `/etc/default/scx` and still want to use them.*

<a id="configuration-sched-ext-learn-more"></a>
### Learn More

> **Note – Credits:**
> Some of the links below were originally referenced from the [sched-ext GitHub repository](https://github.com/sched-ext/scx?tab=readme-ov-file#sched_ext-schedulers-and-tools).
> Full credit goes to the sched-ext maintainers and contributors for curating and sharing these excellent resources.

- [Sched_ext YT playlist](https://youtube.com/playlist?list=PLLLT4NxU7U1TnhgFH6k57iKjRu6CXJ3yB&si=DETiqpfwMoj8Anvl)
- [LWN: The extensible scheduler class (February, 2023)](https://lwn.net/Articles/922405/)
- [arighi's blog: Implement your own kernel CPU scheduler in Ubuntu with sched_ext (July, 2023)](https://arighi.blogspot.com/2023/07/implement-your-own-cpu-scheduler-in.html)
- [David Vernet's talk : Kernel Recipes 2023 - sched_ext: pluggable scheduling in the Linux kernel (September, 2023)](https://youtu.be/8kAcnNVSAdI?si=F5Q-dkSS_sG9BTXA)
- [Changwoo's blog: sched_ext: a BPF-extensible scheduler class (Part 1) (December, 2023)](https://blogs.igalia.com/changwoo/sched-ext-a-bpf-extensible-scheduler-class-part-1/)
- [arighi's blog: Getting started with sched_ext development (April, 2024)](https://arighi.blogspot.com/2024/04/getting-started-with-sched-ext.html)
- [Changwoo's blog: sched_ext: scheduler architecture and interfaces (Part 2) (June, 2024)](https://blogs.igalia.com/changwoo/sched-ext-scheduler-architecture-and-interfaces-part-2/)
- [arighi's YT channel: scx_bpfland Linux scheduler demo: topology awareness (August, 2024)](https://youtu.be/R-FEZOveG-I)
- [David Vernet's talk: Kernel Recipes 2024 - Scheduling with superpowers: Using sched_ext to get big perf gains (September, 2024)](https://youtu.be/Cy7-oqdcUCs?si=bjKu3uidOdIzzAWv)

<a id="configuration-secure-boot-setup"></a>
#### Secure Boot Setup

<a id="configuration-secure-boot-setup-sbctl"></a>
## sbctl

[sbctl](https://github.com/Foxboron/sbctl) is a user-friendly secure boot key manager capable of setting up secure boot,
offering key management capabilities, and keeping track of files that need to be signed in the boot chain.

<a id="configuration-secure-boot-setup-installing-sbctl"></a>
### Installing sbctl

```bash
sudo pacman -S sbctl
```

<a id="configuration-secure-boot-setup-pre-setup"></a>
### Pre-setup

<a id="configuration-secure-boot-setup-grub-boot-manager"></a>
#### GRUB Boot Manager

If you are using GRUB, run the following command to enable secure boot support on GRUB using CA Keys.

```bash
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=cachyos --modules="tpm" --disable-shim-lock
```

> **Note:**
> Loading unnecessary modules in your boot manager has the potential to present a security risk.
> Only run this command if you actually need secure boot.

<a id="configuration-secure-boot-setup-entering-setup-mode-in-uefi"></a>
#### Entering Setup Mode in UEFI
Firstly, we need to go to firmware settings and set secure boot mode to "Setup Mode". You can reboot from an
already running system to firmware settings with following command.

```bash
systemctl reboot --firmware-setup
```

![Image](src/assets/images/ideapad-bios-secure-boot.jpg)

This is how the BIOS looks like on a Lenovo Ideapad 5 Pro. Reset to setup mode or restore factory keys and reboot back
to the system.

However, some MSI motherboards don't have a setup mode. To achieve the same effect, follow the two steps from the image below:

![Image](src/assets/images/MSI-bios-secure-boot.jpg)

<a id="configuration-secure-boot-setup-setting-up-sbctl"></a>
### Setting Up sbctl

```bash
sudo sbctl status # If setup mode is enabled we can proceed to the next step
Installed:      ✘ sbctl is not installed
Setup Mode:     ✘ Enabled
Secure Boot     ✘ Disabled

sudo sbctl create-keys # Create your custom secure boot keys
Created Owner UUID a9fbbdb7-a05f-48d5-b63a-08c5df45ee70
Creating secure boot keys...✔
Secure boot keys created!

sudo sbctl enroll-keys --microsoft # Enroll your keys with Microsoft's keys
Enrolling keys to EFI variables...✔
Enrolled keys to the EFI variables!

sudo sbctl status
# sbctl should now be installed, we can proceed to signing the kernel images and boot manager
Installed:      ✔ sbctl is installed
Owner GUID:     a9fbbdb7-a05f-48d5-b63a-08c5df45ee70
Setup Mode:     ✔ Disabled
Secure Boot     ✘ Disabled
Vendor Keys:    microsoft
```

<a id="configuration-secure-boot-setup-signing-the-kernel-image-and-boot-manager"></a>
### Signing the Kernel Image and Boot Manager

CachyOS provides [sbctl-batch-sign](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/bin/sbctl-batch-sign),
a script that takes the list of files needed to be signed from `sudo sbctl verify` and signs them all.
Limine users should skip to [Limine](#Limine).

```bash
sudo sbctl verify
Verifying file database and EFI images in /boot...
✘ /boot/1c4b5246eef05ac3bc87339323cd5101/6.10.0-cn4.0.fc40.x86_64/linux is not signed
✘ /boot/EFI/BOOT/BOOTX64.EFI is not signed
✘ /boot/EFI/systemd/systemd-bootx64.efi is not signed
✘ /boot/1c4b5246eef05ac3bc87339323cd5101/0-rescue/linux is not signed
✘ /boot/1c4b5246eef05ac3bc87339323cd5101/6.10.0-cn3.0.fc40.x86_64/linux is not signed

sudo sbctl-batch-sign

sudo sbctl verify
Verifying file database and EFI images in /boot...
✔ /boot/1c4b5246eef05ac3bc87339323cd5101/6.10.0-cn4.0.fc40.x86_64/linux is signed
✔ /boot/EFI/BOOT/BOOTX64.EFI is signed
✔ /boot/EFI/systemd/systemd-bootx64.efi is signed
✔ /boot/1c4b5246eef05ac3bc87339323cd5101/0-rescue/linux is signed
✔ /boot/1c4b5246eef05ac3bc87339323cd5101/6.10.0-cn3.0.fc40.x86_64/linux is signed
```

> **Caution:**
> On systems with a separate `/boot` and `/boot/efi` partition layout, `sbctl` may only scan for EFI binaries in `/boot/efi`.
> This causes kernel images that are in `/boot` to not be detected. `sbctl-batch-sign` works around this by **always** scanning
> `/boot` for `vmlinuz-*` files.

Now that all the files are signed, we can reboot back to UEFI settings and enable secure boot.
Note that this is a one-time process as signing files with `-s` flag will save those files to `sbctl`'s database.
`sbctl` ships with a [pacman hook](https://wiki.archlinux.org/title/Pacman_hook) meaning it will automatically
sign all new files upon a kernel or boot manager update.

<a id="configuration-secure-boot-setup-systemd-boot"></a>
#### systemd-boot

CachyOS uses `systemd-boot-update.service` provided by systemd to update the boot manager on reboot. This means that the `sbctl`
pacman hook will **not** sign the updated EFI binaries. As a workaround, we can sign the boot manager directly

```sh
sudo sbctl sign -s -o /usr/lib/systemd/boot/efi/systemd-bootx64.efi.signed /usr/lib/systemd/boot/efi/systemd-bootx64.efi
```

<a id="configuration-secure-boot-setup-limine"></a>
#### Limine

Limine is a special boot manager that allows checking the hash of kernel
images and other files that Limine uses during boot. If this is enabled, any
sort of manual configuration done by the user, e.g. signing the image via
`sbctl-batch-sign`, will modify the hash of the corresponding files and
fail Limine's checksum verification.

However, signing these files isn't necessary on Limine because it has a special
boot process that bypasses EFI chainloading and signature checks. The only EFI
binaries that need to be signed are Limine itself.

```sh
# Use limine-enroll-config to sign Limine's EFI binary
# This uses sbctl under the hood
sudo limine-enroll-config
```

<a id="configuration-secure-boot-setup-verify-that-secure-boot-is-enabled"></a>
### Verify that Secure Boot is Enabled

To check that secure boot is indeed enabled. You can run one of the following commands

```bash
sudo sbctl status
Installed:      ✓ sbctl is installed
Owner GUID:     a9fbbdb7-a05f-48d5-b63a-08c5df45ee70
Setup Mode:     ✓ Disabled
Secure Boot:    ✓ Enabled
Vendor Keys:    microsoft

bootctl
System:
      Firmware: UEFI 2.80 (INSYDE Corp. 28724.16435)
 Firmware Arch: x64
   Secure Boot: enabled (user)
  TPM2 Support: yes
  Measured UKI: no
  Boot into FW: supported
```

<a id="configuration-secure-boot-setup-links-and-credits"></a>
### Links and Credits

- [The Arch Wiki](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Assisted_process_with_sbctl)
laid the groundwork for this guide. Most of the stuff here was taken from there.
- [sbctl](https://github.com/Foxboron/sbctl) - This easy guide to enable secure boot support wouldn't have been possible if it weren't
for the amazing work done to create this piece of software.
- [Improving the Secure Boot Experience by Morten linderud](https://linderud.dev/blog/improving-the-secure-boot-user-experience/) - Blog post by Morten
"Foxboron" Linderud on how the secure boot experience was complicated before `sbctl`.

<a id="configuration-desktop-environments"></a>
### Desktop Environments

<a id="configuration-desktop-environments-hyprland"></a>
##### Hyprland (Deprecated) Keybinds & FAQ

> **Danger – Reference only. CachyOS Hyprland settings has been deprecated.:**

Take a look into our [Hyprland FAQ.](#configuration-desktop-environments-hyprland-faq)

<a id="configuration-desktop-environments-hyprland-keybinds"></a>
### Keybinds

Most of the key combinations require the use of the mod key which in our case is the Windows key (referenced as SUPER), you can change it on the config file.

<a id="configuration-desktop-environments-hyprland-application-control"></a>
#### Application Control

> **Note – CachyOS's Hyprland setup does not include a File Manager by default. Install one you like.:**

| Description | Key |
|-------------|-----|
| Open terminal | `Super+Return` |
| Open Rofi (Program Launcher) | `Super+Space` |
| Open file manager | `Super+E` |
| Close focused window | `Super+Q` |

<a id="configuration-desktop-environments-hyprland-workspace-navigation"></a>
#### Workspace Navigation

| Description | Key |
|-------------|-----|
| Go to workspace (0-9) | `Super+0` through `Super+9` |
| Next workspace | `Super+Period` |
| Previous workspace | `Super+Comma` |
| Move between workspaces with scroll wheel | `Super+Scroll` |
| Switch to previous workspace | `Super+/` |

<a id="configuration-desktop-environments-hyprland-window-navigation"></a>
#### Window Navigation

| Description | Key |
|-------------|-----|
| Focus window up | `Super+ArrowUp` |
| Focus window down | `Super+ArrowDown` |
| Focus window left | `Super+ArrowLeft` |
| Focus window right | `Super+ArrowRight` |
| Change active group | `Super+Tab` |

<a id="configuration-desktop-environments-hyprland-window-management"></a>
#### Window Management

| Description | Key |
|-------------|-----|
| Move window to workspace (0-9) without switching | `Super+Shift+1` through `Super+Shift+9` |
| Move window to workspace (0-9) and switch to it | `Super+Control+1` through `Super+Control+9` |
| Move window up | `Super+Shift+ArrowUp` |
| Move window down | `Super+Shift+ArrowDown` |
| Move window left | `Super+Shift+ArrowLeft` |
| Move window right | `Super+Shift+ArrowRight` |
| Toggle window fullscreen | `Super+F` |
| Toggle window floating | `Super+V` |
| Pin window to all workspaces (floating) | `Super+Y` |
| Toggle window to group | `Super+K` |
| Toggle current window split | `Super+J` |

<a id="configuration-desktop-environments-hyprland-special-workspaces"></a>
#### Special Workspaces
| Description | Key |
|-------------|-----|
| Move active window to Special workspace | `Super+Minus` |
| Toggle Special workspace | `Super+Equal` |
| Call special workspace scratchpad | `Super+F1` |
| Move active window to special workspace scratchpad | `Super+Alt+F1` |

<a id="configuration-desktop-environments-hyprland-window-resizing"></a>
#### Window Resizing

| Description | Key |
|-------------|-----|
| Enter resize mode (use H,J,K,L or arrows, Escape to exit) | `Super+R` |
| Resize window down | `Super+Control+Shift+J` or `Super+Control+Shift+ArrowDown` |
| Resize window up | `Super+Control+Shift+K` or `Super+Control+Shift+ArrowUp` |
| Resize window left | `Super+Control+Shift+H` or `Super+Control+Shift+ArrowLeft` |
| Resize window right | `Super+Control+Shift+L` or `Super+Control+Shift+ArrowRight` |

<a id="configuration-desktop-environments-hyprland-mouse-controls"></a>
#### Mouse Controls

| Description | Key |
|-------------|-----|
| Move window with mouse | `Super+LeftClick` |
| Resize window with mouse | `Super+RightClick` |

<a id="configuration-desktop-environments-hyprland-system-controls"></a>
#### System Controls

| Description | Key |
|-------------|-----|
| Screenshot of area | `Print` |
| Screenshot of active window | `Control+Print` |
| Screenshot of active display | `Alt+Print` |
| Reload Waybar | `Super+O` |
| Lower gap between windows | `Super+G` |
| Reset gaps to default | `Super+Shift+G` |
| Lock screen | `Super+L` |
| Exit Hyprland by terminating the session | `Super+Shift+M` |

<a id="configuration-desktop-environments-hyprland-media-controls"></a>
#### Media Controls

| Description | Key |
|-------------|-----|
| Volume control | Multimedia keys: `VolUp` `VolDown` `Mute` |
| Brightness control | Multimedia keys: depends on hardware |
| Playback control | Multimedia keys:  `Play/Pause` `Next` `Previous` |

<a id="configuration-desktop-environments-hyprland-faq"></a>
### FAQ

<a id="configuration-desktop-environments-hyprland-why-does-my-discord-thunar-and-nautilus-have-a-weird-background"></a>
#### Why does my Discord, Thunar and Nautilus have a weird background?

This is because the window has a modified opacity.

* Consider modifying the window rule in the [Hyprland](https://github.com/CachyOS/cachyos-hyprland-settings/blob/master/etc/skel/.config/hypr/config/windowrules.conf#L21) config file.

```sh title='Example'
windowrulev2 = opacity 0.92, class:^(thunar|nemo)$
```

<a id="configuration-desktop-environments-hyprland-is-there-a-file-manager-included"></a>
#### Is there a File Manager included?

* No, install one you like.

<a id="configuration-desktop-environments-hyprland-what-are-the-reasons-behind-the-deprecation-of-cachyos-hyprland-settings"></a>
#### What are the reasons behind the deprecation of CachyOS Hyprland settings?

Due to the burden of maintaining against the constant upstream changes breaking the configuration + lack of a dedicated maintainer, we have decided to deprecate our Hyprland settings (dotfiles).

<a id="configuration-desktop-environments-i3"></a>
##### i3wm Keybinds & FAQ

Credits go to [vnepogodin](https://github.com/vnepogodin) for making this simple and easy to understand config.

> X11 only, not compatible with Wayland

<a id="configuration-desktop-environments-i3-keybinds"></a>
### Keybinds

Most of the key combinations require the use of the mod key which in our case is the Windows key (referenced as SUPER), you can change it on the config file.

<a id="configuration-desktop-environments-i3-application-control"></a>
#### Application Control

| Description | Key |
|-------------|-----|
| Open terminal | `Super+Return` |
| Open Rofi (Program launcher) | `Control+Space` |
| Kill focused window | `Super+Q` |

<a id="configuration-desktop-environments-i3-workspace-navigation"></a>
#### Workspace Navigation

| Description | Key |
|-------------|-----|
| Go to workspace (1-9) | `Super+1` through `Super+9` |

<a id="configuration-desktop-environments-i3-window-navigation"></a>
#### Window Navigation

| Description | Key |
|-------------|-----|
| Change focus left | `Super+ArrowLeft` |
| Change focus right | `Super+ArrowRight` |
| Change focus up | `Super+ArrowUp` |
| Change focus down | `Super+ArrowDown` |
| Focus last floating/tiling container | `Super+Space` |

<a id="configuration-desktop-environments-i3-window-management"></a>
#### Window Management

| Description | Key |
|-------------|-----|
| Move focused window to workspace (1-9) | `Super+Shift+1` through `Super+Shift+9` |
| Move focused window left | `Super+Shift+ArrowLeft` |
| Move focused window right | `Super+Shift+ArrowRight` |
| Move focused window up | `Super+Shift+ArrowUp` |
| Move focused window down | `Super+Shift+ArrowDown` |
| Toggle fullscreen mode | `Super+F` |
| Toggle floating mode | `Super+Shift+Space` |

<a id="configuration-desktop-environments-i3-layout-control"></a>
#### Layout Control

| Description | Key |
|-------------|-----|
| Split layout horizontally | `Super+H` |
| Split layout vertically | `Super+V` |
| Split toggle | `Super+T` |
| Change container layout to stacking | `Super+S` |
| Change container layout to tabbed | `Super+W` |

<a id="configuration-desktop-environments-i3-resize-mode"></a>
#### Resize Mode

| Description | Key |
|-------------|-----|
| Enter resize mode | `Super+R` |
| Resize left (in resize mode) | `ArrowLeft` |
| Resize right (in resize mode) | `ArrowRight` |
| Resize up (in resize mode) | `ArrowUp` |
| Resize down (in resize mode) | `ArrowDown` |
| Exit resize mode | `Return` / `Escape` / `Super+R` |

<a id="configuration-desktop-environments-i3-system-controls"></a>
#### System Controls

| Description | Key |
|-------------|-----|
| Lock screen | `Super+L` |
| Reload i3 configuration | `Super+Shift+C` |
| Restart i3 in place | `Super+Shift+R` |
| Exit i3 (end X session) | `Super+Shift+E` |
<a id="configuration-desktop-environments-i3-faq"></a>
### FAQ

<a id="configuration-desktop-environments-i3-how-can-create-an-autostart-for-a-program-for-example-set-a-wallpaper-at-start"></a>
#### How can create an autostart for a program? for example "set a wallpaper at start"

* i3 already includes an flexible autostart feature that allows you to execute any program or even commands

If you look at the end of our config file, you'll see some lines starting with exec and exec_always.

For example:

```exec chromium```

This means that Chromium is going to start in workspace 1 whenever you log in into your i3 session.

### What differentiates exec from exec_always?

exec_always gives you the possibility to always execute a certain action even after i3wm got reloaded.

* For more reference and information, checkout their i3's user guide
* https://i3wm.org/docs/userguide.html#exec

### Do the multimedia keys work?

* Yes they do.

For more information about i3wm. Please check out their wiki for reference.

* https://i3wm.org/docs/userguide.html

<a id="configuration-desktop-environments-switch-desktop"></a>
##### Installing another DE/WM using CachyOS Settings

<a id="configuration-desktop-environments-switch-desktop-things-to-consider-before-installing-another-desktop-environment"></a>
### Things to consider before installing another desktop environment

- Having multiple DEs/WMs installed can lead to conflicts, especially with settings managers, default applications, and appearance configurations such as themes and icons in GTK or QT apps.
- The two worst offenders when it comes to conflicts are GNOME and KDE Plasma because they use two completely different toolkits (GTK and QT respectively) and have a lot of background services running that can interfere with other DEs/WMs.
- This fact does not mean that you cannot have them installed together, just be aware that you might run into some issues.
- Package bloat: Mainstream DEs such as GNOME and KDE Plasma could come with hundreds of packages that you might not need or want.
- You can mix many Window Managers with different DEs without much trouble. For example, you can have KDE Plasma and Hyprland installed together and choose which one to use at login.
- CachyOS offered DEs/WMs contain their own respective `-settings` package. For example: `cachyos-i3wm-settings`
- What does this mean? If you wish to install another DE/WM and want to have the same appearance or set of changes we provide, you should install the corresponding `-settings` package.
- These packages place configuration files in `/etc/skel/`, which serves as a template for new user accounts.
- Important: For existing users, these settings **are NOT applied automatically** to prevent overwriting your personal configurations.

<a id="configuration-desktop-environments-switch-desktop-how-to-install-another-dewm-with-cachyos-settings"></a>
### How to install another DE/WM with CachyOS settings

> **Note:**
> You have two choices when installing another DE or WM:
> 1. **Keep your current configuration files** and manually adjust or copy files from `/etc/skel` as needed.
> - For example: if you only want the i3wm configuration files but want to keep your current GTK theme, you can just copy the i3wm related files from `/etc/skel/.config/i3` to your home directory.
> 2. **Overwrite your current configuration files** with the new ones from `/etc/skel/`
> - This gives you the complete CachyOS experience but will replace your current settings.

> **Tip:**
> Take advantage of the Arch Wiki for the respective DE or WM for more in depth information.

1. Create a backup of your current configuration files in your home directory:
    ```bash
    mkdir -p ~/config-backup
    cp -r ~/.config ~/config-backup/
    cp -r ~/.local ~/config-backup/
    ```
2. Uninstall the current `-settings` package if you have one installed. For example, if you are using KDE, run:
    ```bash
    sudo pacman -R cachyos-kde-settings
    ```
> **Note:**
> Removing this package does not remove any of your current DE/WM configurations. It only removes the files stored in `/etc/skel`
3. Install the new DE/WM along with its corresponding `-settings` package. For example, to install i3wm:
    ```bash
    sudo pacman -Syu i3wm cachyos-i3wm-settings
    ```
> **Tip:**
> You can check the list of available DEs/WMs and their corresponding `-settings` packages in the [CachyOS PKGBUILDs GitHub repository](https://github.com/CachyOS/CachyOS-PKGBUILDS)
Or by using your file manager of choice.
4. Copy the new configuration files from `/etc/skel` to your home directory:
- For example: The `cachyos-i3wm-settings` package contains configuration for Kvantum, dunst, GTK, i3, polybar, QT5 and rofi.
- Here is how to do it using a file manager:
    
    1. Open your file manager (Dolphin, Nautilus, Thunar, etc.)
    2. Enable viewing hidden files:
- **Most file managers**: `Ctrl+H` or via a menu: `View` → `Show Hidden Files`
    3. Navigate to `/etc/skel` in the file manager.
    4. Select all files and folders (`Ctrl+A`)
    5. Copy them (`Ctrl+C`)
    6. Navigate to your home directory
    7. Paste the files (`Ctrl+V`)
    8. When prompted about overwriting, choose:
- **"Merge"** or **"Apply to All"** for folders
- **"Replace"** for individual files you want to update
> **Caution:**
> Be careful when replacing files. This will overwrite your current configurations!
    
- Or just use a terminal if you're familiar with it.

After installing the new DE/WM and copying the configuration files, log out of your current session. At the login screen, select the newly installed DE/WM from the session options before logging back in.

<a id="configuration-desktop-environments-switch-desktop-faq"></a>
#### FAQ

<a id="configuration-desktop-environments-switch-desktop-how-to-revert-back-to-my-previous-dewm-configuration"></a>
##### How to revert back to my previous DE/WM configuration?

- Restore from the backup you created:
  ```bash
  cp -r ~/config-backup/.config/* ~/.config/
  cp -r ~/config-backup/.local/* ~/.local/
  ```
  Or by using a file manager.

<a id="configuration-desktop-environments-switch-desktop-what-about-new-updates-to-the-settings-package"></a>
##### What about new updates to the `-settings` package?

- When a `-settings` package updates, the new files are placed in `/etc/skel/`, but your user configuration in `/home/` remains unchanged. To apply updates, you'll need to manually copy the updated files from `/etc/skel/` again.

You'll have to keep an eye on the GitHub repository of the respective DE/WM for any changes.

Here is a list of all the repositories of different DEs and WMs maintained by CachyOS:
- [KDE Plasma](https://github.com/CachyOS/cachyos-kde-settings)
- [Gnome](https://github.com/CachyOS/cachyos-gnome-settings)
- [Niri](https://github.com/CachyOS/cachyos-niri-settings)
- [i3](https://github.com/CachyOS/cachyos-i3wm-settings)
- [Qtile](https://github.com/CachyOS/cachyos-qtile-settings)
- [Wayfire](https://github.com/CachyOS/cachyos-wayfire-settings)

All the other DE and WMs we offer when installing CachyOS don't have their own `-settings` package at the moment. meaning they're just the vanilla versions.

<a id="configuration-desktop-environments-switch-desktop-can-i-keep-multiple-dewm-settings-packages-installed"></a>
##### Can I keep multiple DE/WM settings packages installed?

- Yes and no. You can have multiple DEs/WMs installed, but it's recommended to only have one `-settings` package installed at a time to avoid conflicts in `/etc/skel/`. Otherwise pacman might complain about file conflicts when trying to install another `-settings` package.

<a id="configuration-desktop-environments-switch-desktop-what-are-cachyos-settings"></a>
##### What are "CachyOS Settings"?

"CachyOS Settings" are convenient configuration packages for various desktop environments and window managers. They provide pre-configured settings, themes, and tweaks depending on the DE/WM you choose.

When you install one of these packages . It will also automatically install extra dependencies that are not part of the vanilla DE/WM, such as themes, icons, wallpapers and additional applications. For example in `cachyos-i3wm-settings` we install `rofi`, `dunst`, `picom`, `lxappearance` and more.

<a id="configuration-desktop-environments-kde"></a>
##### KDE Plasma

<a id="configuration-desktop-environments-kde-how-to-install-the-missing-x11-session"></a>
### How to install the missing X11 session

After KDE decided to split their development into multiple packages, the X11 session was removed from the default installation.

```sh
sudo pacman -S plasma-x11-session kwin-x11
```

<a id="configuration-desktop-environments-kde-faq"></a>
### FAQ

<a id="configuration-desktop-environments-kde-how-can-i-get-the-same-look-as-the-one-shown-in-the-kde-screenshots-named-as-emerald"></a>
#### How can I get the same look as the one shown in the KDE Screenshots, named as "Emerald"?

- It's a combination of the Emerald Theme + Qogir Icon Theme which are not installed by default.
- ```sh title='Install both with the following command'
sudo pacman -S cachyos-emerald-kde-theme-git qogir-icon-theme
    ```
  Apply both in `Appearance & Style - Colors & Themes`

### Why does SDDM look so bland and old?

- *Since there is no SDDM theme being applied by default, SDDM will fallback to the classic theme.*
  - **Apply the Breeze Theme as shown in the screenshot**
    

    ![Image](src/assets/images/plasma-sddm-theme.png)

<a id="configuration-desktop-environments-niri"></a>
##### Niri Keybinds & FAQ

> **Note:**
> Niri is a scrollable-tiling Wayland compositor that offers a unique approach to window management with its column-based layout system.

Our main goal with our setup is to have a working Niri configuration that provides a smooth and intuitive desktop experience while keeping the configuration simple and accessible.

Take a look into our [Niri FAQ.](#configuration-desktop-environments-niri-faq)

**Dotfiles maintained by [Ly-sec](https://github.com/Ly-sec)**

<a id="configuration-desktop-environments-niri-keybinds"></a>
### Keybinds

Most of the key combinations require the use of the mod key which in our case is the Windows key (referenced as SUPER), you can change it in the config file.

<a id="configuration-desktop-environments-niri-application-control"></a>
#### Application Control

| Description | Key |
|-------------|-----|
| Open terminal | `Super+Return` |
| Open Wofi (Program Launcher) | `Super+Space` |
| Open browser (Firefox) | `Super+B` |
| Open file manager | `Super+E` |
| Close focused window | `Super+Q` |
| Lock screen | `Super+Alt+L` |

<a id="configuration-desktop-environments-niri-workspace-navigation"></a>
#### Workspace Navigation

| Description | Key |
|-------------|-----|
| Go to workspace (1-9) | `Super+1` through `Super+9` |
| Previous workspace | `Super+Tab` |
| Move between workspaces with scroll wheel | `Super+Scroll` |

<a id="configuration-desktop-environments-niri-window-navigation"></a>
#### Window Navigation

| Description | Key |
|-------------|-----|
| Focus window/column up | `Super+ArrowUp` or `Super+K` |
| Focus window/column down | `Super+ArrowDown` or `Super+J` |
| Focus column left | `Super+ArrowLeft` or `Super+H` |
| Focus column right | `Super+ArrowRight` or `Super+L` |
| Focus first column | `Super+Home` |
| Focus last column | `Super+End` |

<a id="configuration-desktop-environments-niri-monitor-navigation"></a>
#### Monitor Navigation

| Description | Key |
|-------------|-----|
| Focus monitor left | `Super+Shift+ArrowLeft` |
| Focus monitor right | `Super+Shift+ArrowRight` |
| Focus monitor up | `Super+Shift+ArrowUp` |
| Focus monitor down | `Super+Shift+ArrowDown` |

<a id="configuration-desktop-environments-niri-window-management"></a>
#### Window Management

| Description | Key |
|-------------|-----|
| Move window to workspace (1-9) | `Super+Control+1` through `Super+Control+9` |
| Move window/column up | `Super+Control+ArrowUp` or `Super+Control+K` |
| Move window/column down | `Super+Control+ArrowDown` or `Super+Control+J` |
| Move column left | `Super+Control+ArrowLeft` or `Super+Control+H` |
| Move column right | `Super+Control+ArrowRight` or `Super+Control+L` |
| Move column to first position | `Super+Control+Home` |
| Move column to last position | `Super+Control+End` |
| Move column to monitor left | `Super+Shift+Control+ArrowLeft` |
| Move column to monitor right | `Super+Shift+Control+ArrowRight` |
| Move column to monitor up | `Super+Shift+Control+ArrowUp` |
| Move column to monitor down | `Super+Shift+Control+ArrowDown` |

<a id="configuration-desktop-environments-niri-layout-controls"></a>
#### Layout Controls

| Description | Key |
|-------------|-----|
| Expand column to available width | `Super+Control+F` |
| Center column | `Super+C` |
| Center visible columns | `Super+Control+C` |
| Decrease column width | `Super+Minus` |
| Increase column width | `Super+Equal` |
| Decrease window height | `Super+Shift+Minus` |
| Increase window height | `Super+Shift+Equal` |

<a id="configuration-desktop-environments-niri-window-modes"></a>
#### Window Modes

| Description | Key |
|-------------|-----|
| Toggle window floating | `Super+T` |
| Toggle window fullscreen | `Super+F` |
| Toggle column tabbed display | `Super+W` |
| Toggle overview mode | `Super+O` |

<a id="configuration-desktop-environments-niri-screenshots"></a>
#### Screenshots

| Description | Key |
|-------------|-----|
| Screenshot selection | `Control+Shift+1` |
| Screenshot screen | `Control+Shift+2` |
| Screenshot window | `Control+Shift+3` |

<a id="configuration-desktop-environments-niri-system-controls"></a>
#### System Controls

| Description | Key |
|-------------|-----|
| Show hotkey overlay | `Super+Shift+Escape` |
| Emergency escape (restore control) | `Super+Escape` |
| Power off monitors | `Super+Shift+P` |
| Quit Niri | `Control+Alt+Delete` |

<a id="configuration-desktop-environments-niri-media-controls"></a>
#### Media Controls

| Description | Key |
|-------------|-----|
| Volume up | `VolUp` |
| Volume down | `VolDown` |
| Mute audio | `VolMute` |
| Mute microphone | `MicMute` |
| Media next track | `MediaNext` |
| Media previous track | `MediaPrev` |
| Media play/pause | `MediaPlayPause` |

<a id="configuration-desktop-environments-niri-advanced-navigation"></a>
#### Advanced Navigation

| Description | Key |
|-------------|-----|
| Horizontal scroll with mouse | `Super+Scroll Left/Right` |
| Move column with horizontal scroll | `Super+Control+Scroll Left/Right` |
| Alternative column navigation | `Super+Shift+Scroll Up/Down` |
| Move column with alternative scroll | `Super+Control+Shift+Scroll Up/Down` |

<a id="configuration-desktop-environments-niri-faq"></a>
### FAQ

<a id="configuration-desktop-environments-niri-what-makes-niri-different-from-other-window-managers"></a>
#### What makes Niri different from other window managers?

Niri uses a unique scrollable-tiling approach where windows are arranged in columns that can be scrolled horizontally. This provides an infinite desktop metaphor that's particularly useful for ultrawide monitors and workflows requiring many open applications.

<a id="configuration-desktop-environments-niri-how-do-i-change-the-keyboard-layout"></a>
#### How do I change the keyboard layout?

Edit the input section in your config file:

```txt title='Example'
input {
    keyboard {
        xkb {
            layout "us" // Change from "de" to your preferred layout
        }
    }
}
```

<a id="configuration-desktop-environments-niri-can-i-customize-the-gaps-and-window-appearance"></a>
#### Can I customize the gaps and window appearance?

Yes, you can modify the layout section:

```txt title='Example'
layout {
    gaps 8 // Change gap size

    focus-ring {
        width 2
        active-color "#your-color"
        inactive-color "#your-color"
    }
}
```

<a id="configuration-desktop-environments-niri-how-do-i-add-more-startup-applications"></a>
#### How do I add more startup applications?

Add them to the startup section:

```txt title='Example'
spawn-at-startup "your-application"
```

<a id="configuration-desktop-environments-niri-what-is-the-emergency-escape-key-for"></a>
#### What is the emergency escape key for?

The `Super+Escape` binding is designed to restore control when a fullscreen application blocks your keybinds. It disables any active keyboard shortcut inhibitor.

<a id="configuration-desktop-environments-niri-how-do-i-configure-multiple-monitors"></a>
#### How do I configure multiple monitors?

Uncomment and modify the output section for your specific displays. Run `niri msg outputs` to get the correct names:

```txt title='Example'
output "DP-1" {
    mode "1920x1080@60.000"
    scale 1
}
```

<a id="configuration-desktop-environments-qtile"></a>
##### Qtile Keybinds & FAQ

Credits go to [Shendisx](https://github.com/Shendisx) for making this Qtile setup.

> X11 and Wayland session

<a id="configuration-desktop-environments-qtile-keybinds"></a>
### Keybinds

Most of the key combinations require the use of the mod key which in our case is the Windows key (referenced as SUPER), you can change it on the config file.
Some of them might make use of mod1 (ALT key).

<a id="configuration-desktop-environments-qtile-application-control"></a>
#### Application Control

| Description | Key |
|-------------|-----|
| Open terminal | `Super+Return` |
| Open Rofi (Program launcher) | `Alt+Space` |
| Open file manager (Thunar) | `Super+E` |
| Kill focused window | `Super+Q` |

<a id="configuration-desktop-environments-qtile-workspace-navigation"></a>
#### Workspace Navigation

| Description | Key |
|-------------|-----|
| Go to workspace (1-9) | `Super+1` through `Super+9` |

<a id="configuration-desktop-environments-qtile-window-navigation"></a>
#### Window Navigation

| Description | Key |
|-------------|-----|
| Move focus left | `Super+H` |
| Move focus right | `Super+L` |
| Move focus down | `Super+J` |
| Move focus up | `Super+K` |
| Move windows between columns or up/down in stack | `Super+Space` |

<a id="configuration-desktop-environments-qtile-window-management"></a>
#### Window Management

| Description | Key |
|-------------|-----|
| Move focused window left | `Super+Shift+H` |
| Move focused window right | `Super+Shift+L` |
| Move focused window down | `Super+Shift+J` |
| Move focused window up | `Super+Shift+K` |
| Toggle fullscreen | `Super+F` |
| Toggle floating | `Super+V` |
| Stick window (follow between workspaces) | `Super+S` |

<a id="configuration-desktop-environments-qtile-window-resizing"></a>
#### Window Resizing

| Description | Key |
|-------------|-----|
| Grow focused window left | `Super+Control+H` |
| Grow focused window right | `Super+Control+L` |
| Grow focused window down | `Super+Control+J` |
| Grow focused window up | `Super+Control+K` |
| Reset all window sizes to original | `Super+N` |

<a id="configuration-desktop-environments-qtile-layout-control"></a>
#### Layout Control

| Description | Key |
|-------------|-----|
| Toggle between split and unsplit sides of stack | `Super+Shift+Return` |
| Toggle between layouts | `Super+Tab` |

<a id="configuration-desktop-environments-qtile-mouse-controls"></a>
#### Mouse Controls

| Description | Key |
|-------------|-----|
| Drag floating window | `Super+Left_Click` |
| Resize floating window | `Super+Right_Click` |
| Bring window to front | `Super+Scroll_Wheel_Button` |

<a id="configuration-desktop-environments-qtile-screenshot"></a>
#### Screenshot

| Description | Key |
|-------------|-----|
| Execute Flameshot (screenshot utility) | `Print` |
| Capture full-screen screenshot (saved in ~/Pictures) | `Control+Print` |

<a id="configuration-desktop-environments-qtile-system-controls"></a>
#### System Controls

| Description | Key |
|-------------|-----|
| Reload Qtile configuration | `Super+Control+R` |
| Exit Qtile (end X session) | `Super+Control+Q` |
<a id="configuration-desktop-environments-qtile-faq"></a>
### FAQ

<a id="configuration-desktop-environments-qtile-why-is-the-volume-widget-showing-an-error-or-its-stuck-at-0"></a>
#### Why is the volume widget showing an error or it's stuck at 0%?

* This is sometimes due to the Qtile volume widget not being able to detect your default Output Device. You can [take a look in the wiki](https://docs.qtile.org/en/latest/manual/ref/widgets.html#pulsevolume) for more information.

<a id="configuration-desktop-environments-qtile-is-there-a-autostartsh-script"></a>
#### Is there a autostart.sh script?

* Yes, it's located in `scripts/` from Qtile folder.

<a id="configuration-desktop-environments-qtile-does-qtiles-bar-interact-with-the-mouse"></a>
#### Does Qtile's bar interact with the mouse?

* It does, for example if you scroll on the tiny dots which are your workspaces (Active,Inactive,Empty etc) you'll switch to the Left or Right or even click in one of them.
* Another example is the layout (columns by default), clicking on it allows you to switch between the available layouts
* CPU and RAM usage by clicking it's going to open Btop (TUI System Monitor)
* Increase/Lower/Mute/ by interacting on the volume widget

For more information about Qtile, please [check out their wiki](https://docs.qtile.org/en/stable/).

<a id="features-cachy-chroot"></a>
#### CachyOS chroot Helper

[cachy-chroot](https://github.com/CachyOS/cachy-chroot) is a simple helper program to ease the process of chrooting into an existing
CachyOS or Arch-based install. It lists all the partitions discovered on the machine and also supports listing BTRFS subvolumes.
Last but not least, `cachy-chroot` also supports encrypted systems via LUKS. It will map each `fstab` entries to its designated `crypttab`
entries and will gracefully close all LUKS volumes when exiting the chroot.

> **Caution – cachy-chroot is intended to be run from a live CachyOS environment.:**

> **Note:**
> cachy-chroot supports mounting pretty much any filesystem supported by the Linux kernel except for ZFS.

<a id="features-cachy-chroot-usage"></a>
### Usage

> **Tip:**
> Use your arrow keys to navigate the options and `ENTER` to select.
>
> The **❯** symbol indicates the currently selected option.
>
> **?** indicates a prompt for user input.

1. Boot into a live ISO of CachyOS
2. Open a terminal and enter the root user with `sudo su`
3. Make sure you have the latest `cachy-chroot` installed by running:
    ```bash
    pacman -Sy cachy-chroot
    ```
4. Run `cachy-chroot` by typing:
    ```bash
    cachy-chroot
    ```
`cachy-chroot` will scan and list all available partitions.

    
<a id="features-cachy-chroot-example-output-with-cachyos-btrfs-install"></a>
###### Example output with CachyOS BTRFS install

            ```bash
            Info: Found 3 block devices
            Info: Found partition: Partition: /dev/nvme0n1p1: FS: vfat UUID: EDA6-ED98
            Info: Found partition: Partition: /dev/nvme0n1p2: FS: btrfs UUID: b09a027e-a61d-424f-858f-2e02be61b342
            Info: Found partition: Partition: /dev/nvme0n1p4: FS: btrfs UUID: 66e84339-8c77-4131-afce-50ec2cf67a80
            ? Select the block device for the root partition (use arrow keys):  ›
            Partition: /dev/nvme0n1p1: FS: vfat UUID: EDA6-ED98
            ❯ Partition: /dev/nvme0n1p2: FS: btrfs UUID: b09a027e-a61d-424f-858f-2e02be61b342
            ```
    

    
<a id="features-cachy-chroot-example-output-with-ext4"></a>
###### Example output with EXT4

            ```bash
            Info: Found 8 block devices
            Info: Found partition: Partition: /dev/sda1: FS: ext4 UUID: b7fef200-fbb8-4783-9fad-46c5e8b7ca0e
            Info: Found partition: Partition: /dev/sda2: FS: vfat UUID: CA0D-2D5A
            Info: Found partition: Partition: /dev/sdb1: FS: ntfs UUID: A4763F77763F48F6
            Info: Found partition: Partition: /dev/sdc1: FS: ntfs UUID: C4CA216BCA215B46
            Info: Found partition: Partition: /dev/sdc2: FS: ntfs UUID: 060C28590C284651
            Info: Found partition: Partition: /dev/sdc3: FS: ntfs UUID: 3A3CF8B13CF86971
            Info: Found partition: Partition: /dev/sdd1: FS: exfat UUID: 4FDC-0AAB
            Info: Found partition: Partition: /dev/sdd2: FS: vfat UUID: 3105-B091
            ? Select the block device for the root partition (use arrow keys):  ›
            ❯ Partition: /dev/sda1: FS: ext4 UUID: b7fef200-fbb8-4783-9fad-46c5e8b7ca0e
              Partition: /dev/sda2: FS: vfat UUID: CA0D-2D5A
              Partition: /dev/sdb1: FS: ntfs UUID: A4763F77763F48F6
              Partition: /dev/sdc1: FS: ntfs UUID: C4CA216BCA215B46
              Partition: /dev/sdc2: FS: ntfs UUID: 060C28590C284651
              Partition: /dev/sdc3: FS: ntfs UUID: 3A3CF8B13CF86971
              Partition: /dev/sdd1: FS: exfat UUID: 4FDC-0AAB
              Partition: /dev/sdd2: FS: vfat UUID: 3105-B091
            ```
        In this example, the root partition is `/dev/sda1` with `ext4` filesystem. The other partitions are not relevant for the chroot.
    

5. Select the partition that contains the root filesystem:

    
<a id="features-cachy-chroot-example-with-cachyos-btrfs"></a>
###### Example with CachyOS BTRFS

            ```bash title="Selecting root partition"
            ✔ Select the block device for the root partition (use arrow keys):  · Partition: /dev/nvme0n1p2: FS: btrfs UUID: b09a027e-a61d-424f-858f-2e02be61b342
            Info: Selected BTRFS partition, mounting and listing subvolumes...
            Info: Mounting partition /dev/nvme0n1p2 at /tmp/cachyos-chroot-temp-mount-b09a027e-a61d-424f-858f-2e02be61b342-hwAeIm with options: []
            Info: Unmounting partition at /tmp/cachyos-chroot-temp-mount-b09a027e-a61d-424f-858f-2e02be61b342-hwAeIm
            ? Do you want to use CachyOS BTRFS preset to auto mount root subvolume? (y/n) › # Enter yes if on CachyOS
            ```
        **If using CachyOS with BTRFS**, enter `y` to use the CachyOS BTRFS preset. This will automatically mount the root subvolume and other important subvolumes such as `/home`, `/var`, `/tmp` and `/srv`. If you're using a custom BTRFS layout or non-CachyOS system, enter `n` to manually select subvolumes.
    

    
<a id="features-cachy-chroot-example-with-ext4"></a>
###### Example with EXT4

            ```bash title="Selecting root partition"
            ✔ Select the block device for the root partition (use arrow keys):  · Partition: /dev/sda1: FS: ext4 UUID: b7fef200-fbb8-4783-9fad-46c5e8b7ca0e
            Info: Mounting partition /dev/sda1 at /tmp/cachyos-chroot-root-mount-b7fef200-fbb8-4783-9fad-46c5e8b7ca0e-LtsXXC with options: []
            Info: Mounting additional partitions based on /etc/fstab...
            Info: Found 3 entries in /etc/fstab
            Warning: Partition UUID=b7fef200-fbb8-4783-9fad-46c5e8b7ca0e already mounted, skipping...
            Info: Mounting partition /dev/sda2 at /tmp/cachyos-chroot-root-mount-b7fef200-fbb8-4783-9fad-46c5e8b7ca0e-LtsXXC/boot with options: []
            Info: Finished mounting additional partitions
            ✔ Do you want to mount additional partitions? · no
            Info: Chrooting into the configured root partition...
            Info: To exit the chroot, type 'exit' or press Ctrl+D
            ```
    

6. `cachy-chroot` will attempt to automatically mount all the partitions and subvolumes listed under `/etc/fstab` of the root device. If any partitions fail to mount, you will be notified and given the option to mount them manually if needed. You can choose `no` to skip mounting additional partitions.
7. **You are now in the chroot environment**.
    ```bash
    [root@CachyOS /]#
    ```
You can now run commands as if you were booted into the installed system. For example, you can update the system with:
    ```bash title="Updating system in chroot"
    pacman -Syu
    ```
or perform other maintenance tasks as needed.
8. When finished, exit the chroot environment by passing `exit` to the prompt or pressing `CTRL+D` on the keyboard.
    ```bash title="Exiting chroot"
    exit
    ```
9. After exiting, `cachy-chroot` will automatically clean up mounted partitions and close any LUKS containers. You'll return to the live environment shell.

<a id="features-cachy-chroot-troubleshooting"></a>
#### Troubleshooting

- **No partitions found:** Ensure that the disk containing your installation is connected and recognized by the live system. You can check with `lsblk` or `fdisk -l`.
- **Automount fails for some partitions:** You can try mounting them manually from within the chroot environment. `cachy-chroot` will ignore failures and continue.

<a id="features-cachy-chroot-faq"></a>
#### FAQ

- **Q: What is the use for mounting additional partitions?**
- A: There are several use cases for manually mounting additional partitions, including:
- **Broken or missing fstab file:** You can manually mount necessary partitions (such as `/boot` or `/home`) to perform repairs or data recovery.
- **Updated partition UUIDs:** If your system is not booting because you changed the UUID of a prtition, you can use `cachy-chroot` to mount the partitions and then update the fstab accordingly.

<a id="features-cachy-chroot-learn-more"></a>
#### Learn More

- [Arch Wiki - chroot](https://wiki.archlinux.org/title/Chroot)
- [Video demonstration of cachy-chroot](https://github.com/user-attachments/assets/29360aaf-b775-4cfa-9051-465ad5360ae8)

<a id="features-kernel"></a>
#### CachyOS Kernel

The CachyOS Kernel is a customized kernel which utilizes enhancements, configurations and patches from upstream.

<a id="features-kernel-features"></a>
### Features

<a id="features-kernel-performance-optimizations"></a>
#### Performance Optimizations

- **Advanced Compilation**: Highly customizable PKGBUILD with support for both GCC and Clang compilers
- **Link Time Optimization (LTO)**: Thin LTO enabled by default for better performance
- **Profile-Guided Optimization**: AutoFDO + Propeller profiling for optimal code generation ([Learn more](https://cachyos.org/blog/2411-kernel-autofdo/))
- **Kernel Control Flow Integrity (kCFI)**: Available when using LLVM for enhanced security
- **Timer Frequency Options**: Configurable between 300Hz, 500Hz, 600Hz, 750Hz, and 1000Hz (default: 1000Hz)
- **Architecture Optimizations**: Support for x86-64-v3, x86-64-v4, and AMD Zen4 specific builds
- **Compiler Optimizations**: Advanced GCC flags including `-fivopts` and `-fmodulo-sched`

<a id="features-kernel-cpu-enhancements"></a>
#### CPU Enhancements

- **Multiple Schedulers**: BORE, EEVDF, and BMQ schedulers for different workload optimization
- **AMD P-State Enhancements**: Preferred Core support and latest amd-pstate improvements from linux-next
- **Real-Time Support**: RT kernel builds available with BORE scheduler integration
- **CachyOS Sauce**: Custom `CONFIG_CACHY` configuration with scheduler and system tweaks
- **Low-Latency Optimizations**: Patches for improved responsiveness and reduced jitter

<a id="features-kernel-filesystem-memory"></a>
#### Filesystem & Memory

- **ZFS Support**: Built-in ZFS filesystem support with pre-compiled modules
- **NVIDIA Integration**:
- Proprietary NVIDIA driver modules with patches
- Open-source NVIDIA driver support
- Ready-to-use modules in repository
- **I/O Scheduler Improvements**:
- Enhanced BFQ and mq-deadline performance
- Alternative [ADIOS](https://github.com/firelzrd/adios) I/O scheduler support
- **Memory Management**:
- [le9uo](https://github.com/firelzrd/le9uo) patch for preventing page thrashing under memory pressure
- Zen-kernel memory management tweaks (compaction, watermark optimization)

<a id="features-kernel-additional-features"></a>
#### Additional Features

<a id="features-kernel-hardware-support"></a>
##### Hardware Support
- **Gaming Hardware**: Steam Deck patches (Audio, HW Quirks, HID) and ROG Ally support
- **Apple Hardware**: T2 MacBook support included by default
- **ASUS Hardware**: Extended ASUS hardware compatibility patches
- **Graphics**: HDR support enabled, AMDGPU min_powercap override (`amdgpu_ignore_min_pcap`)

<a id="features-kernel-system-enhancements"></a>
##### System Enhancements
- **Multimedia**: v4l2loopback modules included by default
- **Virtualization**: ACS Override support for VFIO/GPU passthrough
- **Upstream Integration**: Cherry-picked patches from Clear Linux and linux-next

<a id="features-kernel-miscellaneous"></a>
##### Miscellaneous

The CachyOS kernel also has some other notable features that are subtle yet improve the user experience:

- Includes a debug variant of the kernel that provides an unstripped kernel binary for debugging purposes. This package is needed to profile the kernel with AutoFDO.
- [Binder](https://developer.android.com/reference/android/os/Binder), the module needed for [Waydroid](https://waydro.id/) is enabled by default in the kernel config
and already [set up](https://github.com/CachyOS/linux-cachyos/blob/master/linux-cachyos/config#L10784).

<a id="features-kernel-variants"></a>
### Variants

CachyOS offers a diverse range of kernel options. All of the kernels we provide are shipped with the [CachyOS Base Patchset](https://github.com/CachyOS/kernel-patches).
For each of the kernels, there is a [corresponding -lto variant](#package-naming-convention) that
is built  with [clang](https://clang.llvm.org/) instead of [GCC](https://gcc.gnu.org/).

- **linux-cachyos**
- The default kernel. This is the recommended kernel if you're unsure which one to use.
- 1000Hz tickrate for improved responsiveness.
- Built with Clang and ThinLTO.
- Profiled with our own [AutoFDO](https://cachyos.org/blog/2411-kernel-autofdo/) profile for improved performance. [Script](https://github.com/CachyOS/cachyos-benchmarker/blob/master/kernel-autofdo.sh) used to profile the kernel.
- **linux-cachyos-bore**
- Uses the [BORE](https://github.com/firelzrd/bore-scheduler) scheduler.
- **linux-cachyos-bmq**
- Uses the BMQ scheduler from [Project C](https://gitlab.com/alfredchen/projectc/) by Alfred Chen.
- `Does not support sched-ext.`
- **linux-cachyos-deckify**
- The default kernel for handhelds. It is **not recommended** and **unsupported** to use any other kernel on handhelds.
- Uses the [BORE](https://github.com/firelzrd/bore-scheduler) scheduler.
- Handheld specific patches on top of the base patchset to improve compatibility and overall experience on handheld devices.
- **linux-cachyos-eevdf**
- Tweaks the default kernel scheduler for improved responsiveness.
- **linux-cachyos-lts**
- Based on the latest Long Term Support kernel.
- Uses the [BORE](https://github.com/firelzrd/bore-scheduler) scheduler.
- Minimally patched compared to other kernels to ensure maximum stability.
- **linux-cachyos-hardened**
- Uses the [BORE](https://github.com/firelzrd/bore-scheduler) scheduler.
- Includes [linux-hardened](https://github.com/anthraxx/linux-hardened) patchset.
- Kernel config based on [linux-hardened config](https://gitlab.archlinux.org/archlinux/packaging/packages/linux-hardened/-/blob/main/config).
- Contains very aggressive hardening that significantly stifles performance and user experience.
- `Does not support sched-ext.`
- **linux-cachyos-rc**
- Based on the latest mainline kernel from [Linus's tree](https://github.com/torvalds/linux/).
- Uses the [BORE](https://github.com/firelzrd/bore-scheduler) scheduler.
- Main kernel to introduce new features in our patchset.
- **linux-cachyos-server**
- Tuned for server workloads compared to desktop usage.
- 300Hz tickrate.
- No preemption.
- Stock EEVDF.
- **linux-cachyos-rt-bore**
- Real-time preemption.
- Uses the [BORE](https://github.com/firelzrd/bore-scheduler) scheduler.

> **Note:**
> Unless otherwise specified, it is safe to assume that all other kernel variants
> have the same configuration as the default kernel.

Please open an issue in [linux-cachyos GitHub](https://github.com/CachyOS/linux-cachyos) for suggestions and improvements that can be added to the default kernel.

<a id="features-kernel-package-naming-convention"></a>
#### Package Naming Convention

```sh
linux-cachyos # Base kernel package for the default kernel. Compiled with Clang and ThinLTO
linux-cachyos-hardened # Base kernel package for the hardened kernel. Compiled with GCC
linux-cachyos-hardened-lto # clang-compiled counterpart for linux-cachyos-hardened
linux-cachyos-hardened-{,lto-}headers
linux-cachyos-hardened-{,lto-}nvidia
linux-cachyos-hardened-{,lto-}nvidia-open
linux-cachyos-hardened-{,lto-}zfs
linux-cachyos-hardened-{,lto-}dbg
```

<a id="features-kernel-prebuilt-kernel-modules"></a>
### Prebuilt Kernel Modules

To accommodate a larger userbase, CachyOS ships some well-known and highly used kernel modules along with the kernel. This means that users will no longer
have to recompile those modules after every kernel update or on every new kernel install, but will only have to install them from the repository as they
are already precompiled. This effectively obsoletes any `-dkms` packages a user might have that provides the same module as the precompiled version.

<a id="features-kernel-zfs"></a>
#### ZFS

[ZFS](https://openzfs.org/wiki/Main_Page) is one of the many filesystems that is supported in CachyOS. Due to it being licensed under
[CDDL](https://opensource.org/license/cddl-1-0), it is incompatible with Linux kernel's license and therefore cannot be merged in-tree. The shipped module includes
the latest upstream features and fixes to ensure compatibility with the latest kernel.

<a id="features-kernel-nvidia"></a>
#### NVIDIA

CachyOS ships both precompiled versions of the close-sourced and [open-sourced](https://github.com/NVIDIA/open-gpu-kernel-modules/) kernel modules. Due to the development
of NVIDIA's kernel module being out-of-tree and thus does not follow the kernel's release cadence, the stock configuration can sometimes be incompatible with the latest
kernel. As a workaround, CachyOS patches the modules with community-created patches or patches shared by NVIDIA directly.

<a id="features-kernel-faq"></a>
### FAQ

<a id="features-kernel-why-is-autofdo-not-being-used-for-all-the-other-kernel-variants"></a>
#### Why is AutoFDO not being used for all the other kernel variants?

Because it's expensive to build since it basically requires building the kernel twice, resulting in more time and resources dedicated to the compilation. The process of building a kernel with AutoFDO involves the following steps:

1) Build the kernel with AutoFDO and debugging capabilities enabled.
2) Create a profile meaning executing workloads in order to gather profiling data for the possible optimizations.
3) Rebuild the kernel with the AutoFDO profile.

Therefore it's only present in the [linux-cachyos](#features-kernel-variants) variant for now.

For more information about AutoFDO, click [here.](https://cachyos.org/blog/2411-kernel-autofdo/)

<a id="features-kernel-does-the-realtime-kernel-improve-gaming-performance"></a>
#### Does the realtime kernel improve gaming performance?

No, it does not. The realtime kernel makes much more code preemptible compared to a normal fully preemptible kernel. This means that much more tasks (gaming processes
included) are frequently preempted and will forcefully yield system resources, leading to worse performance.

<a id="features-cachyos-settings"></a>
#### CachyOS Settings

Alongside our optimized kernels and repositories, we also provide settings that further improve the desktop experience, as well as some
helper scripts for QoL improvements. All these configurations and scripts are under the `cachyos-settings` package.

<a id="features-cachyos-settings-sysctl-tweaks"></a>
### sysctl Tweaks

We provide a lot of sysctl tweaks that aim to improve overall desktop performance. Each sysctl entry is well documented
in the file [99-cachyos-settings.conf](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/sysctl.d/99-cachyos-settings.conf).

To make changes to any of these values, copy the original entry and make a new file under `/etc/sysctl.d/` with the modified value.

<a id="features-cachyos-settings-modifying-sysctl-values"></a>
#### Modifying sysctl values

1. Take a look at the original value from `cachyos-settings`

    ```sh
    cat /usr/lib/sysctl.d/99-cachyos-settings.conf
    # Only experimental!
    # Let Realtime tasks run as long they need
    # sched: RT throttling activated
    kernel.sched_rt_runtime_us=-1
    ```

2. Make a new file in `/etc/sysctl.d` to make changes to the sysctl settings

    ```sh title="Reverting kernel.sched_rt_runtime_us= to its default value"
    sudo micro /etc/sysctl.d/99-kernel-sched-rt.conf # If the file doesn't exist, this command creates and lets you edit the file
    kernel.sched_rt_runtime_us=950000
    ```

<a id="features-cachyos-settings-udev-rules"></a>
### udev Rules

- [ZRAM Rules](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/30-zram.rules) - Sets ZRAM swappiness to a more aggressive
value so cache is more likely to swap to ZRAM
- [HPET Permissions](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/40-hpet-permissions.rules) - Allows access to `rtc0`
and `hpet` device nodes by the audio group
- [SATA Power Management](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/50-sata.rules) - Sets power management policy of SATA devices to `max_performance`
- [I/O Scheduler Rules](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/60-ioschedulers.rules) - Selects the optimal scheduler for each drive type (HDD, SSD, NVMe)
- [hdparm Rules](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/69-hdparm.rules) - Sets SATA and IDE HDDs to maximum performance
- [NVIDIA RTD3](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/71-nvidia.rules) - Configures dynamic power management functionality for the Turing GPU generation. `RTD3 does not work properly on Turing GPUs with the open modules`
- [CPU DMA Latency](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/99-cpu-dma-latency.rules) -
Allows access to the `cpu_dma_latency` device node by the audio group
- [snd_hda_intel PM](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/udev/rules.d/20-audio-pm.rules) - Sets power saving to `0` on AC Power and restores the previous value when switching to Battery

<a id="features-cachyos-settings-modprobe-options"></a>
### modprobe Options

- Forces AMDGPU driver on Southern Islands (GCN 1.0) and Sea Islands (GCN 2.0)
- Enables [various tweaks](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/modprobe.d/nvidia.conf) for NVIDIA
- Blacklists watchdog modules
- Disables power_save for the **sna_hda_intel** audio driver

<a id="features-cachyos-settings-helper-scripts"></a>
### Helper Scripts

- `cachyos-bugreport.sh` - Collects various logs from `inxi`, `dmesg` and `journalctl` to aid in troubleshooting
- `game-performance` - Wrapper script for **`powerprofilesctl`** to switch to performance profile on-demand.
See [Power Profile Switching On Demand](#configuration-gaming-power-profile-switching-on-demand)
- `dlss-swapper` - Wrapper script to force the latest DLSS preset in games that support the technology
- `dlss-swapper-dll` - Like `dlss-swapper`, but requires manually updating the `nvngx_dlss.dll` library shipped with the game; may work with games that have issues with the regular version of the script
- `kerver` - QoL script to show information about the current kernel
- `paste-cachyos` - Script to paste terminal output for text files from the system

    
<a id="features-cachyos-settings-uploading-text-files"></a>
###### Uploading text files

            ```sh
            paste-cachyos /path/to/file
            ```
    

    
<a id="features-cachyos-settings-uploading-terminal-output"></a>
###### Uploading Terminal Output

            ```sh
            &lt;command&gt; | paste-cachyos
            ```
    

- [pci-latency](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/bin/pci-latency) - Reduces latency_timer value to `80` for PCI sound cards and resets all the other PCI devices to `20` and `0`
    ```sh title="Enabling pci-latency system-wide"
    sudo systemctl enable --now pci-latency.service
    ```
- `sbctl-batch-sign` - Helper script to easily sign kernel images and EFI binaries for secure boot and saves them to sbctl's
database
- `topmem` - Shows RAM & swap & ksm stats of 10 processes in a descending order
- `zink-run` - Makes it easier to execute an OpenGL program through Zink Gallium Driver

<a id="features-cachyos-settings-other-configurations"></a>
### Other configurations

<a id="features-cachyos-settings-memory-usage-tweaks"></a>
#### Memory Usage Tweaks

- THP Shrinker configuration `max_ptes_none = 409`
- Set maximum size to `50MB` for the systemd journal
- [ZRAM Generator](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/systemd/zram-generator.conf) - Sets ZRAM to the same size as RAM and use ZSTD for compression

<a id="features-cachyos-settings-ananicy-cpp-rules"></a>
#### Ananicy-cpp Rules

- [ananicy-cpp](https://gitlab.com/ananicy-cpp/ananicy-cpp) with [community-maintained rulesets](https://github.com/CachyOS/ananicy-rules)

<a id="features-cachyos-settings-network-modifications"></a>
#### Network Modifications

- [systemd-resolved as the default DNS Resolver](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/lib/NetworkManager/conf.d/dns.conf) for NetworkManager

<a id="features-cachyos-settings-ntp-qol"></a>
#### NTP QoL

- Preferred server set to `Cloudflare`
- Fallback servers: `Google` and `Arch Linux`

<a id="features-cachyos-settings-systemd-services-tweaks"></a>
#### systemd Services Tweaks

- Timeout for starting a service/unit set to `15s`
- Timeout for stopping a service/unit set to `10s`
- Soft limit for opened file descriptors set to `2048`
- Hard limit for opened file descriptors set to `2097152`

<a id="features-cachyos-settings-xorg"></a>
#### X.Org

- Enable [Tap to Click](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/share/X11/xorg.conf.d/20-touchpad.conf) by default for all X11 sessions

<a id="features-kernel-manager"></a>
#### Managing Linux Kernels & Sched-ext framework with the CachyOS Kernel Manager

Installing a Kernel from a Repository
---------------------------------------

The CachyOS Kernel Manager makes it simple to install and manage kernels from any Arch Linux repository.

To install a kernel. Launch the `CachyOS Kernel Manager` application and choose the desired kernel by ticking the box `[]` from the list of all the available options, then just press `Execute` to start the kernel installation.

To uninstall a kernel, simply uncheck the box `[]` next to the installed kernel you wish to remove and press `Execute` again.

![Image](src/assets/images/cachyos-km1.png)

> **Note:**
> The `Execute` button becomes unavailable when you choose an already installed kernel.

Configuring and Building a custom CachyOS Kernel
---------------------------------

![Image](src/assets/images/cachyos-km2.png)

> **Note:**
> The CachyOS Kernel Manager is specifically designed to build custom kernels for **CachyOS variants** and does not support building or configuring a standard Arch Linux kernel or any other variant.

*To get started. Open the Kernel Manager and click on the `Configure` button to start adjusting various settings, such as the desired scheduler, tick rate and more. Once you have made your desired changes, click on `Build kernel` to begin building your custom CachyOS kernel.*

**Built kernel packages and cache are stored in** `~/.cache/cachyos-km/`

**Available configuration options:**

* `Custom package name`: With this option, you can name your kernel whatever you want. For example: `linux-custom-cachy`
* Scheduler (BORE, RC, RT, RT+BORE, EEVDF and BMQ)
* Enable CachyOS config
* Tweak Configuration via nconfig, menuconfig, xconfig, or gconfig
* Enable/Disable NUMA
* Enable/Disable Modprobed-db
* KBUILD CFLAGS (-O3 or -O2)
* Performance governor as default
* Enable BBR3
* Tick rate selection (100Hz, 250Hz, 300Hz, 500Hz, 600Hz, 750Hz, 1000Hz)
* Tickless mode (idle, periodic, full)
* Preemption (Full, Voluntary or Server)
* Transparent Hugepages (Always or Madvise)
* Enable/Disable DAMON
* Enable/Disable Automatic CPU arch detection
* Apply kernel optimization for specific CPU architectures
* Enable LTO (Full, Thin, No)
* Build ZFS Module
* Build NVIDIA Closed Module
* Build NVIDIA Open Module
* Include vmlinux with debug information/symbols
* Load/Save Kernel Manager config preset: `(Only presets from the manager itself)`
* Kernel Patches Management (Remote and Local support)

*Once the kernel has been successfully built, you will be prompted for your sudo password to install the kernel.*

<a id="features-kernel-manager-sched-ext-framework-management"></a>
### Sched-ext Framework Management

The Kernel Manager provides a graphical user interface (GUI) for managing and controlling sched-ext schedulers. Access the GUI by clicking on the `sched-ext scheduler config` button in the main window.

![Image](src/assets/images/cachyos-km3.png)

This GUI allows you to:

- Switch between different sched-ext (scx) schedulers.
- Enable or disable the scheduler service.
- Check the currently running scheduler.
- Set scheduler flags and profiles.

In order to achieve this, the Kernel Manager uses the `scx_loader` with a configuration stored in `/etc/scx_loader.toml`.

For more information about the `scx_loader` configuration file, check [this documentation](https://github.com/sched-ext/scx/blob/main/tools/scx_loader/configuration.md).

- How does the `scx_loader` work?
- Once you have selected the scheduler and profile, the scx_loader will then start the scheduler with the profile that has been selected and save this configuration to the `/etc/scx_loader.toml` file in order to achieve persistence across reboots. An example of what the file will look like choosing `scx_bpfland` with the `Gaming` profile:
        ```toml
        default_sched = "scx_bpfland"
        default_mode = "Gaming"

        [scheds.scx_bpfland]
        auto_mode = []
        gaming_mode = ["-m", "performance"]
        lowlatency_mode = ["-k", "-s", "5000", "-l", "5000"]
        powersave_mode = ["-m", "powersave"]
        ```

<a id="features-kernel-manager-scheduler-profiles"></a>
#### Scheduler Profiles

- What are the "profiles" for?
- They are presets for the scheduler that modify flags based on proven combinations to enhance effectiveness for specific use cases, such as "Gaming."

<a id="features-kernel-manager-bpfland"></a>
##### Bpfland

**Low Latency**
* **Command-line Flags:** `-s 5000 -S 500 -l 5000 -m performance`
* **Description:** Meant to lower latency at the cost of throughput. Suitable for soft real-time applications like Audio Processing and Multimedia.

**Gaming**
* **Command-line Flags:** `-m performance`
* **Description:** Optimizes performance consistency in games on systems with hybrid cores. Prioritizes P-cores over E-cores on Intel CPUs and CCDs on Ryzen X3D CPUs.

**Power Save**
* **Command-line Flags:** `-m powersave`
* **Description:** Prioritizes power efficiency. Favors less performant cores (e.g E-cores on Intel).

**Server**
* **Command-line Flags:** `-p`
* **Description:** Prioritize tasks with strict affinity. This option can increase throughput at the cost of latency and it is more suitable for server workloads.

<a id="features-kernel-manager-flash"></a>
##### Flash

**Low Latency**
* **Command-line Flags:** `-m performance -w -C 0`
* **Description:** Meant to lower latency at the cost of throughput. Suitable for soft real-time applications like Audio Processing and Multimedia.

**Gaming**
* **Command-line Flags:** `-m all`
* **Description:** Optimizes for high performance in games.

**Power Save**
* **Command-line Flags:** `-m powersave -I 10000 -t 10000 -s 10000 -S 1000`
* **Description:** Prioritizes power efficiency. Favor less performant cores (e.g., E-cores on Intel) and introduces a forced idle cycle every 10ms to increase power saving.

**Server**
* **Command-line Flags:** `-m all -s 20000 -S 1000 -I -1 -D -L`
* **Description:** Tuned for server workloads. Trades responsiveness for throughput.

<a id="features-kernel-manager-lavd"></a>
##### LAVD

**Gaming & Low Latency**
* **Command-line Flags:** `--performance`
* **Description:** Maximizes performance by using all available cores, prioritizing physical cores.

**Power save**
* **Command-line Flags:** `--powersave`
* **Description:** Minimizes power consumption while maintaining reasonable performance. Prioritizes efficient cores and threads over physical cores.

<a id="features-kernel-manager-p2dq"></a>
##### P2DQ

**Gaming**
* **Command-line Flags:** `--task-slice true -f --sched-mode performance`
* **Description:** Improves consistency in gaming performance and increases bias towards scheduling on higher performance cores.

**Low Latency**
* **Command-line Flags:** `-y -f --task-slice true`
* **Description:** Lowers latency by making interactive tasks stick more to the CPU they were assigned to and increasing the stability on slice time.

**Power Save**
* **Command-line Flags:** `--sched-mode efficiency`
* **Description:** Enhances power efficiency by prioritizing power efficient cores.

**Server**
* **Command-line Flags:** `--keep-running`
* **Description:** Improves server workloads by allowing tasks to run beyond their slice if the CPU is idle.

<a id="features-kernel-manager-tickless"></a>
##### Tickless

**Gaming**
* **Command-line Flags:** `-f 5000 -s 5000`
* **Description:** Boosts gaming performance by increasing how often the scheduler detects CPU contention and triggers context switches with a shorter time slice.

**Power Save**
* **Command-line Flags:** `-f 50 -p`
* **Description:** Enhances power efficiency by lowering contention checks and aggressively trying to keep tasks on the same CPU.

**Low Latency**
* **Command-line Flags:** `-f 5000 -s 1000`
* **Description:** Similar to the gaming profile but with a further reduced slice.

**Server**
* **Command-line Flags:** `-f 100`
* **Description:** Reduced how often the scheduler checks for CPU contention to improve throughput at the cost of responsiveness.

<a id="features-kernel-manager-cosmos"></a>
##### Cosmos

**Auto**
* **Command-line Flags:** `-d`
* **Description:** Disables deferred wakeups. Reduces throughput and performance for certain workloads while decreasing power consumption.

**Gaming**
* **Command-line Flags:** `-c 0 -p 0`
* **Description:** Disable CPU load tracking and always enforce deadline-based scheduling to improve responsiveness.

**Power Save**
* **Command-line Flags:** `-m powersave -d -p 5000`
* **Description:** Prioritizes power efficiency. Favor less performant cores (e.g., E-cores on Intel) and disables deferred wakeups, reducing throughput while increasing power efficiency. CPU load polling increased to 5ms.

**Low Latency**
* **Command-line Flags:** `-m performance -c 0 -p 0 -w`
* **Description:** Meant to lower latency at the cost of throughput. Suitable for soft real-time applications like Audio Processing and Multimedia. Always enforce deadline-based scheduling and synchronous wake up optimizations to improve performance predictability.

**Server**
* **Command-line Flags:** `-a -s 20000`
* **Description:** Enable address space affinity to improve locality and performance in certain cache-sensitive workloads. Polling increased to 20ms.

<a id="features-optimized-repos"></a>
#### Optimized Repositories

To deliver a performance-optimized distribution, CachyOS recompiles Arch Linux packages specifically for the `x86-64-v3`, `x86-64-v4`, and `Zen4+` architectures.

- **x86-64-v3:** 5%-20% performance uplift compared to x86-64.
- **x86-64-v4:** Delivers substantial performance gains through AVX512 support, depending on the workload.
- **Zen 4/5:** In addition to the x86-64-v4 instruction set, the following instructions are added:

```text
abm, adx, aes, avx512bf16, avx512bitalg, avx512ifma, avx512vbmi, avx512vbmi2, avx512vnni,
avx512vpopctndq, clflushopt, clwb, clzero, fsgsbase, gfni, mwaitx, pclmul, pku, prfchw,
rpdid, rdrnd, rdseed, sha, sse4a, vaes, vockmulqdq, wbnoinvd, savec, xsaveopt, xsaves
```

To learn more about these architectures, [check this Wikipedia article](https://en.wikipedia.org/wiki/X86-64#Microarchitecture_levels).

<a id="features-optimized-repos-customized-packages"></a>
### Customized Packages

Our [CachyOS-PKGBUILDs](https://github.com/CachyOS/CachyOS-PKGBUILDS) repository contains packages that receive ongoing updates, patches, and backported fixes.
To boost performance, we selectively implement PGO, LTO, and BOLT optimizations depending on the need.
We also maintain a couple of `-git` packages e.g mesa-git.

<a id="features-optimized-repos-cachyos-package-searchhttpspackagescachyosorg"></a>
#### [CachyOS Package Search](<https://packages.cachyos.org/>)

Introducing our new package search page for CachyOS. You can now easily search for packages and access detailed information, such as their compilation architecture, last update date, and more.

![Image](src/assets/images/cachyos-package-dashboard.png)

<a id="features-optimized-repos-migrating-from-x86-64-v3-to-x86-64-v4-or-znver4"></a>
### Migrating from x86-64-v3 to x86-64-v4 or znver4

If you’re currently using the x86-64-v3 repositories and your new CPU supports x86-64-v4 (or AMD Zen 4/5), you can migrate by following these steps:

<a id="features-optimized-repos-checking-cpu-compatibility"></a>
#### Checking CPU Compatibility

> **Caution:**
> Intel 12th gen (Alder Lake) and newer CPUs may report `x86-64-v4` support, but in practice they **cannot run AVX-512 instructions**.
>
> Why?
> - **Hybrid architecture conflict**: The big “P-cores” support AVX-512, but the small “E-cores” do not. Running AVX-512 while E-cores are active would cause instability.
> - **Intel’s workaround**: To avoid this mismatch, Intel disabled AVX-512 in two ways:
> - **Microcode/BIOS updates** (early Alder Lake chips): AVX-512 could be re-enabled by avoiding or rolling back microcode updates.
> - **Hardware fusing** (later 2022+ chips): AVX-512 is permanently disabled at the factory, making it impossible to re-enable.
>
> Because `x86-64-v4` requires AVX-512, these CPUs should be treated as **x86-64-v3 only**.

- Verifying `x86-64-v4` support:
  ```sh title='Run the following command:'
  /lib/ld-linux-x86-64.so.2 --help | grep supported
  ```
- ✅ `x86-64-v4 (supported, searched)` → CPU supports v4
- ❌ No `x86-64-v4` line → CPU does not support v4

Example (CPU supports v4):
  ```sh
  $ /lib/ld-linux-x86-64.so.2 --help | grep supported
    x86-64-v2 (supported, searched)
    x86-64-v3 (supported, searched)
    x86-64-v4 (supported, searched)
  ```

- For AMD Zen 4/5 CPUs, check if your CPU reports znver4 or znver5:
- Run the following command:
    ```sh
    gcc -march=native -Q --help=target 2>&1 | grep -Po "^\s+-march=\s+\K(\w+)\$"
    ```
If the output is `znver4` or `znver5`, you can proceed with the migration.

> **Note:**
> Both x86-64-v4 and znver4 use the same mirrorlist `/etc/pacman.d/cachyos-v4-mirrorlist`.

> **Note – If you need to go back to a repository or revert the change, this guide will be useful to you.:**
> Example: From znver4 to v4.

<a id="features-optimized-repos-migration-steps"></a>
#### Migration Steps

1. Edit `/etc/pacman.conf` and replace your `x86-64-v3` repositories with one of the following depending on your CPU support:

    
<a id="features-optimized-repos-x86-64-v4"></a>
###### x86-64-v4

            ```ini title='/etc/pacman.conf'
            [cachyos-v4]
            Include = /etc/pacman.d/cachyos-v4-mirrorlist

            [cachyos-core-v4]
            Include = /etc/pacman.d/cachyos-v4-mirrorlist

            [cachyos-extra-v4]
            Include = /etc/pacman.d/cachyos-v4-mirrorlist
            ```
    

    
<a id="features-optimized-repos-znver4-amd-zen-45-only"></a>
###### znver4 (AMD Zen 4/5 only)

          ```ini title='/etc/pacman.conf'
          [cachyos-znver4]
          Include = /etc/pacman.d/cachyos-v4-mirrorlist

          [cachyos-core-znver4]
          Include = /etc/pacman.d/cachyos-v4-mirrorlist

          [cachyos-extra-znver4]
          Include = /etc/pacman.d/cachyos-v4-mirrorlist
        ```
    

    Keep `[cachyos]`, `[core]`, `[extra]`, and `[multilib]` unchanged.
    
2. Clear the package cache and synchronize databases:

   ```sh
   sudo pacman -Scc   # Confirm with 'y' twice
   sudo pacman -Sy
   ```

3. Reinstall all packages to switch to the new architecture:

   ```sh
   pacman -Qqn | sudo pacman -S -
   ```

4. Reboot your system.

---

<a id="features-optimized-repos-adding-our-repositories-to-an-existing-arch-linux-install"></a>
### Adding Our Repositories to an Existing Arch Linux Install

> **Caution:**
> Installing the CachyOS Pacman will install a forked pacman with features added from CachyOS, like "INSTALLED_FROM" and an automatic architecture check. Pacman 6.1 added a feature validation feature, which could lead when using the Arch Linux pacman into warnings. We are working with Arch Linux to provide a proper compatibility again. If you want to avoid this, don't add the "cachyos" repository, which contains the customized pacman. All other repositories like cachyos-v3, cachyos-v4, cachyos-extra/core-v3/4 are safe to add.

> **Tip:**
> Before considering adding our repositories, please take a look at the **[CPU compatibility list](#installation-installation-prepare-x8664-microarchitecture-level-support)**

<a id="features-optimized-repos-automated"></a>
###### Automated

We provide a script that automates the installation of our repositories to your existing Arch-based installs.

```sh
curl https://mirror.cachyos.org/cachyos-repo.tar.xz -o cachyos-repo.tar.xz
tar xvf cachyos-repo.tar.xz && cd cachyos-repo
sudo ./cachyos-repo.sh
```

> **Tip – How the script works:**
> This script detects the instruction sets your CPU is capable of and installs whichever version of our repositories that
> is most optimized for it. It also backs up your old `pacman.conf` for repository removal via the script.

<a id="features-optimized-repos-manual"></a>
###### Manual

1. Install CachyOS keyring:

   ```sh
   # Import the repository key
   sudo pacman-key --recv-keys F3B607488DB35A47 --keyserver keyserver.ubuntu.com
   # Sign the repository key
   sudo pacman-key --lsign-key F3B607488DB35A47
   ```
2. Install the necessary packages:

   ```sh
   sudo pacman -U 'https://mirror.cachyos.org/repo/x86_64/cachyos/cachyos-keyring-20240331-1-any.pkg.tar.zst' \
   'https://mirror.cachyos.org/repo/x86_64/cachyos/cachyos-mirrorlist-22-1-any.pkg.tar.zst' \
   'https://mirror.cachyos.org/repo/x86_64/cachyos/cachyos-v3-mirrorlist-22-1-any.pkg.tar.zst' \
   'https://mirror.cachyos.org/repo/x86_64/cachyos/cachyos-v4-mirrorlist-22-1-any.pkg.tar.zst' \
   'https://mirror.cachyos.org/repo/x86_64/cachyos/pacman-7.0.0.r7.g1f38429-2-x86_64.pkg.tar.zst'
   ```
3. Add the CachyOS repositories to the pacman config file:
> **Note:**
> These repositories should be put above Arch Linux Repositories.

   ```ini
   # /etc/pacman.conf
   # If your CPU only supports x86-64, then add the [cachyos] repositories
   # cachyos repos
   [cachyos]
   Include = /etc/pacman.d/cachyos-mirrorlist

   # If your CPU supports x86-64-v3, then add [cachyos-v3],[cachyos-core-v3],[cachyos-extra-v3] and [cachyos]
   # cachyos repos

   [cachyos-v3]
   Include = /etc/pacman.d/cachyos-v3-mirrorlist
   [cachyos-core-v3]
   Include = /etc/pacman.d/cachyos-v3-mirrorlist
   [cachyos-extra-v3]
   Include = /etc/pacman.d/cachyos-v3-mirrorlist
   [cachyos]
   Include = /etc/pacman.d/cachyos-mirrorlist

   # If your CPU supports x86-64-v4, then add [cachyos-v4], [cachyos-core-v4], [cachyos-extra-v4] and [cachyos]
   # cachyos repos

   [cachyos-v4]
   Include = /etc/pacman.d/cachyos-v4-mirrorlist
   [cachyos-core-v4]
   Include = /etc/pacman.d/cachyos-v4-mirrorlist
   [cachyos-extra-v4]
   Include = /etc/pacman.d/cachyos-v4-mirrorlist
   [cachyos]
   Include = /etc/pacman.d/cachyos-mirrorlist

   # If your CPU is based on Zen 4 or Zen 5, add [cachyos-znver4], [cachyos-core-znver4], [cachyos-extra-znver4] and [cachyos]

   [cachyos-znver4]
   Include = /etc/pacman.d/cachyos-v4-mirrorlist
   [cachyos-core-znver4]
   Include = /etc/pacman.d/cachyos-v4-mirrorlist
   [cachyos-extra-znver4]
   Include = /etc/pacman.d/cachyos-v4-mirrorlist
   [cachyos]
   Include = /etc/pacman.d/cachyos-mirrorlist
   ```
> **Tip:**
> In order to make the transition from the `v4` repositories to the `znver4`
>
> Add the corresponding entries from the previous step and execute the following commands:
> ```sh
> sudo pacman -Scc # Enter Y in both instances
> sudo pacman -Sy
> pacman -Qqn | sudo pacman -S - # To replace all the v4 packages with the znver4 packages
> # Reboot your system
> ```

4. Finally, update your system with CachyOS packages:
   ```sh
   sudo pacman -Syu
   ```

<a id="features-optimized-repos-uninstalling-cachyos-repositories"></a>
#### Uninstalling CachyOS Repositories

<a id="features-optimized-repos-automated"></a>
###### Automated

**Run the following commands to remove the CachyOS repositories from your system:**
```sh
curl https://mirror.cachyos.org/cachyos-repo.tar.xz -o cachyos-repo.tar.xz
tar xvf cachyos-repo.tar.xz
cd cachyos-repo
sudo ./cachyos-repo.sh --remove
```

<a id="features-optimized-repos-manual"></a>
###### Manual

1. Reinstall the original pacman from Arch Linux:
   ```sh
   sudo pacman -S core/pacman
   ```
2. Execute the following command:
   ```sh
   # This avoids getting %INSTALLED_DB% warnings
   sudo find /var/lib/pacman/local/ -type f -name "desc" -exec sed -i '/^%INSTALLED_DB%$/,+2d' {} \;
   ```
3. Restore the pacman config file from backup:
   ```sh
   sudo mv /etc/pacman.conf.bak /etc/pacman.conf
   ```
4. Switch back to the default Arch Linux packages with the following commands:
   ```sh
   pacman -Qqn | sudo pacman -S -
   sudo pacman -Syu
   ```

<a id="features-optimized-repos-tests-and-benchmarks"></a>
### Tests and benchmarks

Michael from Phoronix has already benchmarked CachyOS a couple of times, which is shown mostly leading in the benchmark graphs and on the Geometric Mean of All Test Results.
Since the first benchmark made back in 2022, CachyOS has evolved and matured a lot more in terms of usability and performance.

If you would like to know more about the performance uplift from our repositories, please check the links below.

* **14/03/2021:** In a RFC discussion about the impact of x86-64-v3 was started by **Mateusz Jończyk** from Arch Linux showed some initial results.
* [RFC: Use x86_64-v2 architecture](https://lists.archlinux.org/pipermail/arch-general/2021-March/048739.html)

* **09/12/2022:** First benchmark done by Michael.
* [The Performance Of Arch Linux Powered CachyOS](https://www.phoronix.com/review/cachyos-linux-perf)

* **29/02/2024:** Phoronix conducted another benchmark demonstrating the difference between x86-64-v4, x86-64-v3 and x86-64 (generic) Packages. Looking at the examples like PHP or GCC, where we customize our PKGBUILDs there is a noticeable performance improvement.
* [Arch Linux CachyOS Benchmarks Of x86-64-v3 & x86-64-v4 Repositories](https://www.phoronix.com/review/cachyos-x86-64-v3-v4)

* **20/08/2024:** Michael posted a new benchmark for the AMD Ryzen 9950x on which it includes CachyOS and some others Linux Distributions.
* [Intel Continues To Show AMD The Importance Of Software Optimizations: 16% More Ryzen 9 9950X Performance](https://www.phoronix.com/review/linux-os-amd-ryzen9-9950x)
> **Note:**
> Liquid-DSP and RocksDB were compiled using the Phoronix Benchmark Suite, ignoring the compilation flags specified in /etc/makepkg.conf resulting in unexpected performance results for CachyOS.

<a id="features-chwd"></a>
### Chwd

<a id="features-chwd-chwd"></a>
##### Managing Hardware with chwd

[CachyOS Hardware Detection](https://github.com/CachyOS/chwd/) (better known as `chwd`) enables us to power a variety of hardware by installing the necessary
packages and drivers for the running system. This includes systems running NVIDIA's graphics cards, T2 Macbooks, and handheld devices such as the Steam Deck and ROG Ally.

<a id="features-chwd-chwd-usage"></a>
### Usage

`chwd` is typically ran during installation time to provide the necessary packages for the system. However, it is also possible
to use it post-install.

<a id="features-chwd-chwd-auto-configuration"></a>
#### Auto Configuration

`chwd` supports installing and configuring necessary drivers and packages so that the system can work at optimal conditions.

```sh
sudo chwd -a
```

<a id="features-chwd-chwd-installing-a-profile"></a>
#### Installing a profile

An alternative to the above method is to install each specific profile.

```sh title='List all available profiles'
chwd --list-all
╭─────────────────────────┬─────────╮
│ Name                    ┆ NonFree │
╞═════════════════════════╪═════════╡
│ nvidia-open-dkms.prime  ┆ true    │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ nvidia-dkms             ┆ true    │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ macbook-t2              ┆ false   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ phoenix                 ┆ false   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ steam-deck              ┆ false   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ amd                     ┆ false   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┤
│ intel                   ┆ false   │
╰─────────────────────────┴─────────╯
```

```sh title='Installing a chwd profile'
sudo chwd -i amd
> Installing amd ...

> Successfully installed amd
```

<a id="features-chwd-chwd-others"></a>
#### Others

Consult the help output of `chwd` for command syntax and other usage.

```sh
chwd --help
Usage: chwd [OPTIONS]

Options:
  -i, --install &lt;profile&gt;          Install profile
  -r, --remove &lt;profile&gt;           Remove profile
  -d, --detail                     Show detailed info for listings
  -f, --force                      Force reinstall
      --list-installed             List installed kernels
      --list                       List available profiles for all devices
      --list-all                   List all profiles
  -a, --autoconfigure [&lt;classid&gt;]  Autoconfigure
      --ai_sdk                     Toggle AI SDK profiles
      --pmcachedir &lt;PMCACHEDIR&gt;    [default: /var/cache/pacman/pkg]
      --pmconfig &lt;PMCONFIG&gt;        [default: /etc/pacman.conf]
      --pmroot &lt;PMROOT&gt;            [default: /]
  -h, --help                       Print help
  -V, --version                    Print version
```

<a id="features-chwd-gpu-migration"></a>
##### Switching Between NVIDIA and AMD GPUs

> **Note – This guide applies if you are replacing your GPU (NVIDIA ↔ AMD) on an existing CachyOS installation.:**

<a id="features-chwd-gpu-migration-prerequisites"></a>
### Prerequisites
- Your replacement GPU is properly installed and connected.
- Ensure your system is fully up to date
    ```bash
    sudo pacman -Syu
    ```

<a id="features-chwd-gpu-migration-migration-steps"></a>
#### Migration Steps

<a id="features-chwd-gpu-migration-from-nvidia-to-amd"></a>
###### From NVIDIA to AMD

    While the AMD drivers are included in the Linux Kernel, you may need to clean up the old NVIDIA configuration and ensure that the necessary AMD packages are installed.
    
        1. Check which NVIDIA driver profile is currently installed:
                ```bash
                sudo chwd --list-installed
                ```
        2. Remove the specific profile using the `-r` flag:
                ```bash
                sudo chwd -r &lt;profile-name&gt;
                ```
        3. Shutdown your system and proceed to install your AMD GPU.
        4. After booting. Use chwd to automatically detect your GPU and install the correct AMD packages.
                ```bash
                sudo chwd -a
                ```
        5. After installing the new drivers, update your initramfs and bootloader configuration
            > CachyOS includes a pacman hook that automatically rebuilds initramfs when drivers are added or removed.
            > This ensures the correct drivers are loaded at boot.
- GRUB: `sudo grub-mkconfig -o /boot/grub/grub.cfg`
- systemd-boot: `sudo sdboot-manage gen`
- Limine: `sudo limine-mkinitcpio`
        6. Reboot to apply changes.
                ```bash
                sudo reboot
                ```
        7. After rebooting, verify that the AMD drivers are active.
                ```bash
                vulkaninfo | grep "deviceName"
                ```
            or
                ```bash
                glxinfo | grep "OpenGL renderer"
                ```
            If you see your AMD GPU listed, the drivers are working correctly.
    

<a id="features-chwd-gpu-migration-from-amd-to-nvidia"></a>
###### From AMD to NVIDIA

    
        1. Clean the remaining AMD packages.
                ```bash
                sudo chwd -r amd
                ```
        2. Shutdown your system and proceed to install your NVIDIA GPU.
        3. After booting. Use chwd to automatically detect your GPU and install the correct NVIDIA packages.
                ```bash
                sudo chwd -a
                ```
        4. After installing the new drivers, update your initramfs and bootloader configuration
            > CachyOS includes a pacman hook that automatically rebuilds initramfs when drivers are added or removed.
            > This ensures the correct drivers are loaded at boot.
- GRUB: `sudo grub-mkconfig -o /boot/grub/grub.cfg`
- systemd-boot: `sudo sdboot-manage gen`
- Limine: `sudo limine-mkinitcpio`
        5. Reboot to apply changes.
                ```bash
                sudo reboot
                ```
        6. After rebooting, verify that the NVIDIA drivers are active.
                ```bash
                nvidia-smi
                ```
            or
                ```bash
                glxinfo | grep "OpenGL renderer"
                ```
            If you see your NVIDIA GPU listed, the drivers are working correctly.

<a id="installation-desktop-environments"></a>
#### Desktop Environments

CachyOS offers several desktop environments for you to choose from.

This decision is based on personal preference. Pick one that you like the most.
> **Note:**
> Please select only one Desktop Environment during the installation.

The available options are:

1. **KDE Plasma:** a comprehensive and flexible desktop environment that offers multiple styles of menus to access applications. It features the KWin window manager. KDE Plasma also boasts an intuitive interface that allows you to easily download and install new themes, widgets, and more from the web.
2. **GNOME:** a user-friendly desktop environment with a touch-style interface for accessing applications. While it is easy to learn, it has limited customization options and can be difficult to configure.
3. **XFCE:** a lightweight and flexible desktop environment with a traditional drop-down/pop-up menu for accessing applications. It is also compatible with Compiz.
4. **bspwm:** a C-based X11 window manager offering flexible tiling, stacking, and tabbing layouts.
5. **Budgie:** a simple and elegant desktop environment built using the GTK toolkit. It is designed to provide a modern and attractive interface that is easy to use while also being highly configurable.
6. **Cinnamon:** a desktop environment for Linux that balances advanced features with a traditional user experience.
7. **Cosmic:** `Currently in beta.` a modern, performance-oriented desktop environment built with Rust and Smithay. Designed for productivity and power users, it aims to offer advanced features while maintaining a clean but intuitive interface.
8. **i3:** a popular X11 tiling window manager known for its single, self-contained configuration file and its efficient use of screen space. Find our i3 [dotfiles here](https://github.com/CachyOS/cachyos-i3wm-settings).
9. **Hyprland:** a visually pleasing Wayland compositor that uses dynamic tiling. It comes with pre-configured [dotfiles](https://github.com/CachyOS/cachyos-hyprland-settings).
10. **LXDE** (Lightweight X11 Desktop Environment): a fast and energy-saving desktop environment designed to be used on older computers and resource-constrained systems. It uses Openbox as its default window manager and focuses on providing a simple, clean and user-friendly interface.
11. **LXQt:** a lightweight desktop environment formed from the merger of the LXDE and Razor-qt projects and built with Qt.
12. **Mate Desktop:** a traditional desktop environment forked from GNOME 2. It is characterized by its classic look and feel, with a simple and intuitive user interface. Mate provides an easy-to-use and highly customizable desktop experience for users who prefer a more classic look and feel.
13. **Openbox:** a highly popular X11 window manager known for its excellent documentation and a wide selection of available themes.
14. **Qtile:** a X11/Wayland window manager that is configured with the Python programming language. Offers various layouts and widgets. Find our [dotfiles here](https://github.com/CachyOS/cachyos-qtile-settings).
15. **Sway:** a tiling Wayland compositor and a drop-in replacement for the i3 window manager for X11. It works with your existing i3 configuration and supports most of i3's features plus a few extras.
16. **UKUI:** a lightweight desktop environment that is efficient and works well on older computers. It uses both GTK and Qt technologies, and has a visual appearance similar to Windows 7, making it user-friendly for new Linux users.
17. **Wayfire:** a Wayland compositor based on wlroots that balances customization, extensibility, and aesthetics. Find our Wayfire [dotfiles](https://github.com/CachyOS/cachyos-wayfire-settings).
18. **Niri:** is a scrollable tiling Wayland compositor that emphasizes simplicity and fluid window management. It uses a continuous grid layout, optimized for both keyboard and touchpad navigation. Find our Niri [dotfiles](https://github.com/CachyOS/cachyos-niri-settings).

> **Note:**
> Due to the nature of Hyprland including breaking changes and instability, we decided to maintain our dotfiles without providing official assistance in support channels.
>
> Therefore, try asking for help in our Discord instead and wait for an answer from the community.

<a id="installation-desktop-environments-screenshots"></a>
### Screenshots

*Section for images showcasing our theming and designs to the provided desktop environments and window managers.*

<a id="installation-desktop-environments-kde"></a>
#### KDE
> CachyOS Breeze

![Image](src/assets/images/plasma-default.png)

> Emerald Theme

![Image](src/assets/images/emerald1920x180guest1.png)
![Image](src/assets/images/emerald1920x180guest3.png)
![Image](src/assets/images/emerald1920x180guest4.png)

> CachyOS Nord Theme

![Image](src/assets/images/nord1920x180guest1.png)
![Image](src/assets/images/nord1920x180guest.png)
![Image](src/assets/images/nord1920x180guest2.png)
![Image](src/assets/images/nord1920x180guest3.png)
![Image](src/assets/images/nord1920x180guest4.png)

<a id="installation-desktop-environments-gnome"></a>
#### Gnome

![Image](src/assets/images/gnome.png)
![Image](src/assets/images/gnome1.png)

<a id="installation-desktop-environments-i3"></a>
#### i3

![Image](src/assets/images/i3.png)

<a id="installation-desktop-environments-xfce"></a>
#### XFCE

![Image](src/assets/images/xfce.png)

<a id="installation-desktop-environments-cosmic"></a>
#### Cosmic

![Image](src/assets/images/cosmic.png)

<a id="installation-desktop-environments-openbox"></a>
#### OpenBox

![Image](src/assets/images/openbox.png)

<a id="installation-desktop-environments-lxqt"></a>
#### LXQT

![Image](src/assets/images/lxqt.png)

<a id="installation-desktop-environments-hyprland"></a>
#### Hyprland

![Image](src/assets/images/hyprland1.png)

<a id="installation-desktop-environments-ukui"></a>
#### UKUI

![Image](src/assets/images/ukui.png)

<a id="installation-desktop-environments-cinnamon"></a>
#### Cinnamon

![Image](src/assets/images/cinnamon.png)

<a id="installation-desktop-environments-budgie"></a>
#### Budgie

![Image](src/assets/images/budgie.png)

<a id="installation-desktop-environments-mate"></a>
#### Mate

![Image](src/assets/images/mate.png)

<a id="installation-desktop-environments-lxde"></a>
#### LXDE

![Image](src/assets/images/lxde.png)

<a id="installation-desktop-environments-niri"></a>
#### Niri

![Image](src/assets/images/niri.jpg)

<a id="installation-filesystem"></a>
#### Filesystems

CachyOS offers 5 different filesystems to allow the user to choose what best fits their needs. The following will go over advantages, disadvantages, and recommendations for each filesystem. Each filesystem comes with its requirements/utilities preinstalled on CachyOS.

> **Note:**
> BTRFS is the default and recommended filesystem for CachyOS. Choose it if unsure.

<a id="installation-filesystem-xfs"></a>
### XFS

XFS is a journaling filesystem created and developed by Silicon Graphics, Inc. It was created in 1993, ported to linux in 2001, and is now widely supported by most Linux distributions.

<a id="installation-filesystem-pros"></a>
#### Pros

- Fast, XFS was originally designed with speed and extreme scalability in mind.
- Reliable, XFS makes use of several technologies to prevent data corruption.
- Resistant to fragmentation due to its extent-based nature and delayed allocation strategy.

<a id="installation-filesystem-cons"></a>
#### Cons

- Cannot be shrunk.

<a id="installation-filesystem-userspace-utility"></a>
#### Userspace utility

The package containing userspace tools to manage XFS filesystems is `xfsprogs`.

<a id="installation-filesystem-recommendation"></a>
#### Recommendation

XFS is the recommended filesystem for users who do not need advanced features and simply want a fast and reliable filesystem.

<a id="installation-filesystem-btrfs"></a>
### BTRFS

BTRFS is a modern copy-on-write(COW) filesystem created in 2007 and declared stable in the linux kernel in 2013. It is widely supported and is mainly known for its advanced feature set.

<a id="installation-filesystem-pros"></a>
#### Pros

- Transparent compression. BTRFS supports transparently compressing files to allow for significant space savings with no user intervention. **CachyOS ships with ZSTD compression set to level 3 by default.**
- Snapshot functionality. BTRFS leverages its COW nature to allow for the creation of snapshots of subvolumes that take up very little actual space.
- Subvolume functionality allowing for greater control over the filesystem.
- Able to grow or shrink.
- Very fast development.

<a id="installation-filesystem-cons"></a>
#### Cons

- Sometimes requires defragmentation or balancing.
- Worse on rotational drives due to aforementioned fragmentation.

<a id="installation-filesystem-userspace-utility"></a>
#### Userspace utility

Btrfs userspace utility package is `btrfs-progs`

<a id="installation-filesystem-subvolume-layout"></a>
#### Subvolume Layout

CachyOS provides a subvolume layout out of the box to allow easy snapshot functionality.

- Subvol @ = /
- Subvol @home = /home
- Subvol @root = /root
- Subvol @srv = /srv
- Subvol @cache = /var/cache
- Subvol @tmp = /var/tmp
- Subvol @log = /var/log

<a id="installation-filesystem-recommendation"></a>
#### Recommendation

BTRFS is recommended for users who want snapshot/backup functionality and transparent compression.

<a id="installation-filesystem-ext4"></a>
### EXT4

EXT4 (fourth extended filesystem) is the most commonly used Linux filesystem. EXT4 was made stable in the linux kernel in 2008.

<a id="installation-filesystem-pros"></a>
#### Pros

- Very common, allowing easy access to plenty of resources.
- Reliable. EXT4 has a proven track record of being very reliable.
- Able to grow or shrink.
- Shrinking is only supported offline and requires the filesystem to be unmounted.

<a id="installation-filesystem-cons"></a>
#### Cons

- Built on an old code base.
- Lacks many of the advanced features other filesystems offer.

<a id="installation-filesystem-userspace-utilities"></a>
#### Userspace utilities

The package to manage ext4 is `e2fsprogs`

<a id="installation-filesystem-recommendation"></a>
#### Recommendation

EXT4 is recommended for users who want the simplest and most commonly used filesystem.

<a id="installation-filesystem-zfs"></a>
### ZFS

ZFS is an advanced filesystem originally developed by Sun Microsystems in 2005. ZFS has many features, but is licensed under CDDL which means it cannot be included inside the linux kernel and requires a separate module installed.

> **Caution:**
> Do not use a Real-time kernel together with ZFS, it's not compatible due to licensing issues.

<a id="installation-filesystem-pros"></a>
#### Pros

- Pooled storage (zpool)
- Snapshots using COW
- Compression
- Raid-Z support
- ARC cache allows insanely fast read times on commonly accessed files.

<a id="installation-filesystem-cons"></a>
#### Cons

- Very complicated to use and understand due to features like zpool and ARC.
- ARC requires a lot of ram to be effective.
- Not included in the linux kernel therefore dependent on a third party kernel module (OpenZFS)
- Incompatible with Real-time preemption

<a id="installation-filesystem-required-tools"></a>
#### Required tools

'ZFS-Module' CachyOS provides a precompiled zfs module for each kernel version.
`zfs-utils` for the userspace utilities.

<a id="installation-filesystem-recommendation"></a>
#### Recommendation

ZFS should only be used by advanced users who want to use its advanced features, such as pooled storage or the ARC cache.

<a id="installation-filesystem-f2fs"></a>
### F2FS

F2FS (Flash-Friendly File System) is a flash file system originally created and developed by Samsung for the linux kernel. F2FS was created to cater specifically for the NAND flash used in modern day storage.

<a id="installation-filesystem-pros"></a>
#### Pros

- Designed with flash friendliness in mind.
- Transparent compression used to reduce disk writes (space savings not currently usable by the user).
- Faster than other filesystems like EXT4.
- Better wear leveling, which further prolongs the life of NAND flash.

<a id="installation-filesystem-cons"></a>
#### Cons

- Cannot shrink.
- Space savings from compression cannot currently be used by the user. This may be added in the future.
- Relatively weak fsck (filesystem check).
- Downgrading to a kernel older than the version that created the filesystem may cause issues.
- Requires a workaround when used with GRUB on MBR/BIOS system.

<a id="installation-filesystem-userspace-utilities"></a>
#### Userspace utilities

The main utility for f2fs is `f2fs-tools`

<a id="installation-filesystem-recommendation"></a>
#### Recommendation

- F2FS is recommended for users who want to maximize the lifespan of their NAND flash devices.
- Limine is the recommended bootloader for F2FS users on MBR/BIOS systems since it does not require a workaround like GRUB does.

<a id="installation-filesystem-bcachefs"></a>
### BcacheFS

Bcachefs is an advanced new filesystem for Linux, with an emphasis on reliability and robustness and the complete set of features one would expect from a modern filesystem.

> **Caution – ATTENTION:**
> Bcachefs is still considered as experimental and may have issues.

<a id="installation-filesystem-pros"></a>
#### Pros

- Copy on write (CoW) - like BTRFS or ZFS
- Compression
- Caching, Data Placement
- Replication
- Scalable

<a id="installation-filesystem-cons"></a>
#### Cons

- Experimental
- Setup can be complicated

<a id="installation-filesystem-tldr"></a>
### TL:DR

Use the default filesystem **BTRFS** as it is considered stable and has a lot of neat features (snapshots, compression, etc). Use **XFS** or **EXT4** for a simple
and fast filesystem.

<a id="installation-installation-handheld"></a>
#### Handheld Edition

CachyOS provides an edition for handheld devices, such as the Steam Deck, ROG Ally, and Legion Go. This edition offers a SteamOS-like experience with Game Mode Switching, pre-installed Gaming Applications, and more.

The Handheld Edition employs the LAVD scheduler as the default CPU scheduler, which is optimized for handheld devices. This results in improved frame rates and battery life during gaming.

The Handheld Edition uses `systemd-boot` as the boot manager. Boot manager selection is not available
as opposed to the default CachyOS ISO. This is intended to simplify the installation process.

> **Note – KDE Plasma is the only supported desktop environment for the Handheld Edition.:**

<a id="installation-installation-handheld-installation-on-root"></a>
### Installation on Root

1. **Download** the latest Handheld ISO from the website/forum.

2. [Flash](#installation-installation-prepare) the ISO.

3. **Boot** into the ISO.

4. Click the **Launch Installer** Button.

5. Calamares will now open. Follow the on-screen instructions.

6. At the partition step, please use the **Erase Disk** option. If you come from another Linux distribution, it may have been using a different partition layout. Be aware that the replace partition option can be problematic and might not work as expected.

7. Install the System.

After the installation is completed. Calamares will prompt you to reboot the device.

The first boot can take a bit of time, since Steam is getting downloaded and started.
This process can take up to 2 minutes.

<a id="installation-installation-handheld-installation-with-dual-boot"></a>
### Installation with Dual Boot

1. **Download** the latest Handheld ISO from the website/forum.

2. [Flash](#installation-installation-prepare) the ISO.

3. **Boot** into the ISO.

4. Click the **Launch Installer** Button.

5. Calamares will now open. Follow the on-screen instructions.

6. At the partition step you need to select **Manual Partition** and create following partitions:

- 2GB /boot
- XGB / (X can be any number of storage space you wish to allocate to the root filesystem)

7. Proceed with the steps and install the system.

After the installation is completed, Calamares will prompt you to reboot the device.

The first boot can take a bit of time, since Steam is getting downloaded and started.
This process can take up to 2 minutes.

<a id="installation-boot-managers"></a>
#### Offered Boot Managers

To offer the best experience across a range of devices, CachyOS currently offers the following boot managers: **systemd-boot, rEFInd, GRUB, and Limine**.

This wiki article describes the feature set of each boot manager and includes our recommendations for when to choose them.
For configuration, please see [Boot Manager Configuration](#configuration-boot-manager-configuration).

> **Caution:**
> **Important Note:** Some MSI motherboards have UEFI firmware that does not fully comply with the UEFI specification. This can lead to compatibility issues with certain boot managers, including GRUB and rEFInd.
>
> If you encounter such issues, consider using `systemd-boot` or `Limine`.

---

<a id="installation-boot-managers-quick-feature-comparison"></a>
### Quick Feature Comparison

| Feature | systemd-boot | rEFInd | GRUB | Limine |
| --- | --- | --- | --- | --- |
| Firmware support | UEFI only (no BIOS/MBR) | UEFI only | UEFI & BIOS | UEFI & BIOS |
| /boot<br>filesystem support | According to firmware's support (usually FAT12/16/32); More with EFI drivers | Firmware's,ext2,ext3,ext4,btrfs,ISO-9660,HFS+, and NTFS; More with EFI drivers | Broad filesystem support (ext*, Btrfs, XFS, etc.) | FAT12/16/32, ISO9660 for<br>/boot |
| Windows dual-boot | Auto-detects Windows Boot Manager on the same ESP | Auto-detects EFI loaders and kernels | Supported via<br>os-prober<br>or manual config | Supported; Windows Boot Manager entries can be added with<br>limine-scan |
| Btrfs snapshot integration | Possible with custom setup (not provided by CachyOS) | Possible with custom setup (not provided by CachyOS) | Supported on CachyOS via<br>grub-btrfs-support | Supported on CachyOS via<br>limine-snapper-sync |
| Full Disk Encryption (FDE) | Possible (root encrypted;<br>/boot<br>must remain unencrypted) | Possible (root encrypted;<br>/boot<br>must remain unencrypted) | Fully supported, including encrypted<br>/boot<br>via<br>cryptodisk<br>(LUKS1/PBKDF2 only; LUKS2 support limited/workarounds needed) | Possible (root encrypted;<br>/boot<br>must remain unencrypted) |
| Theming / UI | Minimal, no theming | Graphical, themeable UI | Themeable, classic UI | Themeable menu (skins) |
| Ease of setup on CachyOS | Very simple (CachyOS auto-configures it by default) | Easy setup with automatic OS and kernel detection | Simplified by CachyOS hooks/scripts (includes Btrfs snapshots in menu) | Simplified by CachyOS tools (entry helpers + snapshot menu integration) |
| MSI UEFI quirks | Works reliably | Can have issues (workarounds required) | Can have issues | Works reliably |
| Best use case | Fast/simple UEFI setups; fallback for MSI quirks | Multi-boot with polished UI | Needed for encrypted<br>/boot<br>, BIOS, or widest FS support | Modern setups wanting snapshot booting + BIOS & UEFI + chainloading |

<a id="installation-boot-managers-boot-manager-details"></a>
### Boot Manager Details

<a id="installation-boot-managers-systemd-boot"></a>
#### systemd-boot

Part of the systemd family, systemd-boot was created to be as simple as possible. Therefore, it only has support for UEFI-based systems. This simple yet efficient design ensures it is reliable and fast, but it comes at the cost of advanced features supported by other boot managers.

<a id="installation-boot-managers-pros"></a>
##### Pros
- Very simple configuration.
- Boot entries are separated into multiple files, making them easy to manage.
- Ensures compatibility with some MSI boards that face UEFI issues when using other boot managers.
- On CachyOS, configuration is auto-generated out of the box.

<a id="installation-boot-managers-cons"></a>
##### Cons
- No support for BIOS/MBR.
- Very barebones: no theming or customization.
- If using a boot filesystem beyond the firmware's default ones (FAT12/16/32), then separate ESP and [XBOOTLDR](https://wiki.archlinux.org/title/Systemd-boot#Installation_using_XBOOTLDR) partitions & EFI drivers need to be manually added.
- Cannot find boot images on partitions other than its own ESP or the XBOOTLDR partition.
- Config is not auto-generated unless configured to do so.
- No native support for Btrfs snapshot rollbacks due to requirement to store kernel images on the boot partition rather than the root.
- Snapshot booting is possible only with custom setups (not provided by CachyOS).

---

<a id="installation-boot-managers-refind"></a>
#### rEFInd

A fork of rEFIt, rEFInd was primarily made to make it easier for MacOS users to multi-boot. However, rEFInd has evolved into being hardware agnostic, making it a great choice for multi-booting on any system. The main draw of rEFInd is its ability to scan all storage devices at boot and correspondingly display entries for each OS/Kernel found.

<a id="installation-boot-managers-pros"></a>
##### Pros
- Autodetects all operating systems and kernels on storage devices.
- Little to no manual configuration required.
- Graphical UI reminiscent of the MacOS boot selector.
- Great theming support, with optional touchscreen support.
- Can read boot images from EFI filesystems (FAT12/16/32) as well as EXT4 and BTRFS. Additional filesystem support can be enabled by installing EFI drivers from the `efifs` package.

<a id="installation-boot-managers-cons"></a>
##### Cons
- No support for BIOS systems.
- Incompatible with some MSI boards (due to UEFI spec violations).
- Fixable with a workaround, but requires extra steps.

---

<a id="installation-boot-managers-grub"></a>
#### GRUB

GRUB is the oldest of the available boot managers. It has a very large feature set, works on almost every machine, and remains the most widely used Linux boot manager.

<a id="installation-boot-managers-pros"></a>
##### Pros
- Supports nearly all Linux filesystems.
- Widely used — documentation and community help are abundant.
- Supports encrypted `/boot` partitions.
- Supports Btrfs snapshot booting (via `grub-btrfs-support` on CachyOS).
- Supports BIOS and UEFI systems.
- Theme support available, despite the somewhat dated UI.

<a id="installation-boot-managers-cons"></a>
##### Cons
- Large and complex, with many filesystem drivers.
- Noticeably slower than systemd-boot, rEFInd, and Limine.
- Incompatible with some MSI boards (UEFI spec violations).

---

<a id="installation-boot-managers-limine"></a>
#### Limine

Limine is a modern, advanced, and portable multiprotocol bootloader. It serves as the reference implementation for the Limine boot protocol and supports Linux as well as chainloading other loaders.

<a id="installation-boot-managers-pros"></a>
##### Pros
- Supports multiple boot protocols, including Multiboot2 and the Linux boot protocol.
- Can boot on both UEFI and BIOS systems.
- Has theming capabilities similar to GRUB.
- Supports Btrfs snapshots via `limine-snapper-sync`, enabled by default on CachyOS with Btrfs.

<a id="installation-boot-managers-cons"></a>
##### Cons
- `/boot` must use FAT12/16/32 or ISO9660. Other filesystems require additional setup.
- Does not automatically add an entry to UEFI NVRAM. This must be done manually with `efibootmgr`, or handled automatically with `limine-entry-tool` (preinstalled on CachyOS).
- Does not work with UFS (Universal Flash Storage), used e.g. in some Chromebooks.

---

<a id="installation-boot-managers-tldr"></a>
### TL;DR

- Choose GRUB if you need encrypted `/boot`, BIOS compatibility, or want Btrfs snapshots with a stable, mature boot manager.

- Choose Limine if you want a modern bootloader with Btrfs snapshot integration out of the box, plus support for both BIOS and UEFI and Windows dual-boot (via **limine-scan**).

- Choose rEFInd if you want a polished graphical interface and automatic multi-boot detection on UEFI systems.

- Choose systemd-boot if you prefer the simplest setup and don’t require snapshots or advanced features. It’s also the most reliable fallback for MSI motherboards with UEFI issues.

<a id="installation-installation-prepare"></a>
#### Preparation steps

<a id="installation-installation-prepare-system-requirements"></a>
### System Requirements

Before preparing the installation, make sure that the computer used meets the minimum system requirements in order to run CachyOS. The installer
uses an online installation process so a stable and relatively fast internet connection is mandatory.

> **Note – Virtual Machines:**
> It is not recommended to install CachyOS on a virtual machine. VMs can have issues with incorrect configuration or can be broken entirely. It is recommended to install CachyOS on bare metal.

<a id="installation-installation-prepare-minimum-requirements"></a>
###### Minimum requirements

*   3 GB RAM
*   30 GB of Storage Space (HDD/SSD)
*   Stable internet connection

> **Caution:**
> Unstable internet may result in extended installation times or failed installations in the worst case.

<a id="installation-installation-prepare-recommended-requirements"></a>
###### Recommended requirements

*   8GB RAM
*   50 GB of Storage Space (SSD/NVMe)
*   [x86-64-v3 capable CPU](#installation-installation-prepare-x8664-microarchitecture-level-support)
*   50 Mbps or better internet speed
*   NVIDIA GPU (900+ - e.g: GTX 950), AMD +GCN 1.0 (e.g: AMD R7 240) or Intel (Integrated HD Graphics series or higher. Arc Series)

<a id="installation-installation-prepare-x8664-microarchitecture-level-support"></a>
### x86_64 Microarchitecture Level Support

| x86-64 ABI | CPU Families / Examples |
| --- | --- |
| x86-64-v3 | AMD Family 15h (Excavator)<br>AMD Family 17h (Zen)<br>AMD Family 17h (Zen+)<br>AMD Family 17h (Zen 2)<br>AMD Family 19h (Zen 3)<br>Intel 4th Gen Core (Haswell)<br>Intel 5th Gen Core (Broadwell)<br>Intel 6th Gen Core (Skylake)<br>Intel 7th Gen Core (Kaby Lake)<br>Intel 8/9th Gen Core (Coffee Lake)<br>Intel 10th Gen Core (Comet Lake)<br>Intel 12th Gen (Alder Lake)<br>Intel 13th Gen (Raptor Lake)<br>Intel 14th Gen (Raptor Lake Refresh)<br>Intel 15th Gen (Lunar / Arrow Lake) |
| x86-64-v4 | AMD Family 19h (Zen 4 / Zen 4c)<br>AMD Family 1Ah (Zen 5 / Zen 5c)<br>Intel 6th Gen Core (Skylake X)<br>Intel 8th Gen Core i3 (Cannon Lake)<br>Intel Xeon / 10th Gen Core (Ice Lake)<br>Intel Xeon (Cascade Lake)<br>Intel Xeon (Cooper Lake)<br>Intel 3rd Gen 10nm++ (Tiger Lake)<br>Intel 4th Gen 10nm++ (Sapphire Rapids)<br>Intel 5th Gen 10nm++ (Emerald Rapids)<br>Intel 11th Gen (Rocket Lake) |

<a id="installation-installation-prepare-creating-a-bootable-cachyos-usb-drive"></a>
### Creating a Bootable CachyOS USB Drive

There are several tools and methods that can be used to create a bootable USB drive of CachyOS.

> **Note:**
> The USB drive must have at least 8GB of available space.

<a id="installation-installation-prepare-balenaetcher"></a>
#### balenaEtcher

1. Download [balenaEtcher](<https://etcher.balena.io/>). balenaEtcher supports flashing an image of Linux, MacOS and Windows.
   If a `.zip` file was downloaded, extract it and execute the binary using the following commands:
      ```sh
      # Extract zip file:
      bsdtar xvf &lt;zip file name&gt;
      # cd to the new folder:
      cd balenaEtcher-linux-x64/
      # Execute balenaEtcher:
      ./balena-etcher
      ```
2. Plug in a USB drive to the computer.
3. Select `Flash from file` and select the CachyOS ISO image file.
4. Click `Select target` and choose the USB drive that was previously plugged in.
5. Press `Flash` to start the flashing process.

> **Note:**
> balenaEtcher may prompt for administrator privileges. If so, enter your password and click on `Authenticate`.

![Image](src/assets/images/etcher.png)

<a id="installation-installation-prepare-command-line-interface-linux-macos"></a>
#### Command Line Interface (Linux & MacOS)

1. Plug in a USB drive.
2. Detect the plugged USB drive using the following commands:
   ```sh
   # Linux
   # The USB drive could be identified e.g: /dev/sda, by disk model and size.
   sudo fdisk -l

   # MacOS
   # USB drives are identified as "/dev/diskY" where "Y" could be 0,1 etc.
   diskutil list
   ```
3. Copy the iso contents to the plugged-in USB drive by running:
   ```sh
   # Replace &lt;usbdrive&gt; with the label of the drive.
   sudo dd bs=4M if=full_iso_name.iso of=/dev/&lt;usbdrive&gt; status=progress oflag=sync
   ```

- `dd` will now copy the contents of the ISO file over to the plugged-in USB drive.

<a id="installation-installation-prepare-rufus-windows-only"></a>
#### Rufus (Windows Only)

1. Plug in a USB drive.
2. Download [Rufus](<https://rufus.ie/>) and install it, or run the portable version.
3. On `Device`, click on the dropdown list and select the plugged-in USB drive.
4. On `Boot selection`, click on `SELECT` and locate the CachyOS ISO image file.
5. Click `START`.

<a id="installation-installation-prepare-ventoy-linux-windows"></a>
#### Ventoy (Linux & Windows)

<a id="installation-installation-prepare-linux"></a>
###### Linux

1. Plug in a USB drive.
2. Download [Ventoy](<https://www.ventoy.net/en/download.html>)
3. Untar Ventoy using the following command:
   ```sh
   # Replace version with the correct one e.g: ventoy-1.1.07-linux.tar.gz
   bsdtar xvf ventoy-version-linux.tar.gz
   # cd to the new folder: (version might change)
   cd ventoy-1.1.07/
   ```
4. Execute `VentoyGUI.x86_64` by either double clicking on it or via the terminal:
   ```sh
   # It will ask for administrative privileges, enter your credentials
   ./VentoyGUI.x86_64
   ```
5. Select the plugged-in USB drive by clicking on `Device`.
6. Click on `Install`.
7. After it finishes installing Ventoy into the plugged-in USB drive, close the window and place the CachyOS ISO file into the new usable partition of the drive.

<a id="installation-installation-prepare-windows"></a>
###### Windows

1. Plug in a USB drive.
2. Download [Ventoy](<https://www.ventoy.net/en/download.html>)
3. Run `Ventoy2Disk.exe`
4. Select the plugged-in USB drive by clicking on `Device`.
5. Click on `Install`.
6. After it finishes installing Ventoy into the USB drive, close the window and place the CachyOS ISO file into the new usable partition of the drive.

<a id="installation-installation-t2macbook"></a>
#### T2 MacBook

CachyOS provides out-of-the-box support for T2 MacBooks, including necessary kernel patches in all provided kernels. However, there are crucial steps required to ensure a successful setup.

> **Caution – Potential Risks:**
> Completely removing macOS carries risks, like data loss or rendering the device unusable. It's **strongly recommended** to keep a macOS partition for firmware updates and recovery. Refer to the [T2 Linux Roadmap](https://wiki.t2linux.org/roadmap/#can-i-completely-remove-macos) for details.
>
> If you still decide to remove macOS, ensure you have a full backup and create a [bootable macOS installer](https://support.apple.com/en-us/101578) beforehand.

<a id="installation-installation-t2macbook-pre-installation"></a>
### Pre-Installation

Creating a bootable macOS installer is optional but recommended if you plan to modify partitions or remove macOS. It can be useful for firmware updates, troubleshooting, or system restoration. For detailed instructions, refer to [Apple's guide](https://support.apple.com/en-us/101578).

Perform these steps below within macOS **before** booting the CachyOS installer.

<a id="installation-installation-t2macbook-prepare-cachyos-bootable-usb"></a>
#### Prepare CachyOS Bootable USB

Download the [CachyOS ISO](#cachyos-basic-download) and follow the instructions in [Creating a Bootable CachyOS USB Drive](#installation-installation-prepare-creating-a-bootable-cachyos-usb-drive) to create the installation media.

<a id="installation-installation-t2macbook-optional-extract-wi-fi-firmware"></a>
#### (Optional) Extract Wi-Fi Firmware

> **Note:**
> Wi-Fi **will not work** out of the box during or after installation because the required firmware is proprietary and cannot be redistributed by CachyOS. You will need an internet connection (e.g., Ethernet, USB tethering) for the installation process unless you follow the steps below to prepare the Wi-Fi firmware beforehand and enable it during installation.

While still in macOS, open Terminal and run the following command. This copies the necessary Wi-Fi firmware files to your EFI partition, making them accessible later during the CachyOS installation.
```sh
curl -sL https://wiki.t2linux.org/tools/firmware.sh | bash -s copy_to_efi
```

<a id="installation-installation-t2macbook-prepare-your-disk"></a>
#### Prepare Your Disk

If you plan to dual-boot with macOS (recommended), you need to create space for CachyOS. Use the Disk Utility application in macOS to resize your existing macOS partition:

1.  Open **Disk Utility**.
2.  In the Disk Utility sidebar, select the **volume** you want to resize (usually named "Macintosh HD" or similar).
3.  Click the **"Partition"** button in the toolbar.
4.  Click the **"+" (plus)** button below the pie chart representing your disk usage.
5.  **Crucially**, when prompted, choose **"Add Partition"**, *not* "Add Volume". You need to create a separate partition for Linux.
6.  **Name:** Enter a descriptive name for the new partition (e.g., "CachyOS" or "Linux").
7.  **Format:** Select any available format (like APFS or Mac OS Extended). The CachyOS installer will reformat this partition later, so the initial choice doesn't matter.
8.  **Size:** Allocate the desired amount of storage space for CachyOS. **Be aware that resizing partitions later can be difficult or impossible**, so choose a size that meets your needs.
10. Click **"Apply"** to create the new partition. Disk Utility will resize your macOS partition and create the new empty space.

<a id="installation-installation-t2macbook-disable-secure-boot"></a>
#### Disable Secure Boot

1. Reboot your Mac and hold `Command (⌘) + R` immediately after powering on to enter Recovery Mode.
2. Go to Utilities > Startup Security Utility.
3. Select "No Security" under **Secure Boot** and "Allow booting from external or removable media" under **Allowed Boot Media**.

Refer to [Apple's guide on Startup Security Utility](https://support.apple.com/en-in/102522) for more details.

---

For an additional overview of preparing a T2 Mac for Linux, consult the [t2linux Preinstall guide](https://wiki.t2linux.org/guides/preinstall/).

<a id="installation-installation-t2macbook-installation-process"></a>
### Installation Process

1.  **Boot from CachyOS USB:**
*   Restart your Mac and hold the `Option (⌥)` key immediately after powering on.
*   Select the CachyOS USB drive (usually labeled as "EFI Boot").
2.  **(Optional) Enable Wi-Fi in the Live Environment:**
*   If you need Wi-Fi during installation and don't have Ethernet/tethering, open the terminal once the CachyOS live environment loads.
*   Run these commands to copy the firmware from the EFI partition (created in [Extract Wi-Fi Firmware](#optional-extract-wi-fi-firmware)) and configure the NetworkManager:
        ```sh
        # Mount the EFI partition (usually nvme0n1p1 on T2 Macs)
        sudo mkdir -p /tmp/apple-wifi-efi
        sudo mount /dev/nvme0n1p1 /tmp/apple-wifi-efi

        # Copy firmware from EFI to the live environment
        bash /tmp/apple-wifi-efi/firmware.sh get_from_efi
        sudo umount /tmp/apple-wifi-efi

        # Configure NetworkManager to use iwd backend
        cat <<EOF | sudo tee /etc/NetworkManager/conf.d/wifi_backend.conf
        [device]
        wifi.backend=iwd
        EOF
        sudo systemctl restart NetworkManager
        ```
*   You should now be able to connect to Wi-Fi networks using the network applet in the system tray.
3.  **Run the CachyOS Installer:**
*   Launch the CachyOS installer from the desktop or application menu.
*   Follow the standard installation procedure, referring to the [Installation on Root](#installation-installation-on-root) guide.
*   When partitioning, select the free space created earlier. Let the installer handle formatting.
> **Caution – Partitioning Caution:**
> Be **very careful** during the partitioning step in the installer. Ensure you are selecting the correct free space you prepared and **do not** accidentally delete or format your existing macOS partition, especially if you intend to dual-boot. Double-check your selections before proceeding.
*   CachyOS Hardware Detection ([chwd](#features-chwd)) should automatically apply necessary T2-specific boot parameters and configurations during installation.

<a id="installation-installation-t2macbook-post-installation-steps"></a>
### Post-Installation Steps

After the installation is complete and you have rebooted into your new CachyOS system, you may need to perform a few additional steps to ensure everything works smoothly.

<a id="installation-installation-t2macbook-install-wi-fi-firmware-permanently"></a>
#### Install Wi-Fi Firmware Permanently

If you have followed the optional [Enable Wi-Fi in the Live Environment](#installation-process) step to get firmware in the live ISO, you can simply follow it again to enable Wi-Fi. Otherwise connect to the internet (e.g., Ethernet, USB tethering) and follow the steps below:

1. Open a terminal and download the firmware package from the Arch Linux T2 mirror:
   ```sh
   curl https://mirror.funami.tech/arch-mact2/os/x86_64/apple-bcm-firmware-14.0-1-any.pkg.tar.zst -o apple-bcm-firmware-14.0-1-any.pkg.tar.zst
   ```
2. Install the downloaded package:
   ```sh
   sudo pacman -U apple-bcm-firmware-14.0-1-any.pkg.tar.zst
   ```
3. Reload the Wi-Fi kernel modules:
   ```bash
   sudo modprobe -r brcmfmac_wcc
   sudo modprobe -r brcmfmac
   sudo modprobe brcmfmac
   ```

Wi-Fi should now work reliably after reboots. You can remove the downloaded `.pkg.tar.zst` file.

<a id="installation-installation-t2macbook-further-configuration"></a>
#### Further Configuration
For configuring other hardware components like audio, webcam, Touch Bar, etc., refer to the various guides on the [t2linux Wiki](https://wiki.t2linux.org/roadmap/#configuring-the-installation).

<a id="installation-installation-on-root"></a>
#### CachyOS Installation Desktop/Laptop

<a id="installation-installation-on-root-before-you-begin"></a>
### Before you begin

> **Note – If you only get GRUB and Limine as boot manager options after pressing Launch Installer, then the system is booted in Legacy/BIOS mode.:**

> **Danger – Installing multiple desktop environments is not allowed during the installation process.:**

> **Caution – Secure Boot and CSM must be disabled in the BIOS/UEFI settings when installing in UEFI mode.:**
> To setup Secure Boot after installation, refer to the [Secure Boot](#configuration-secure-boot-setup) section.
>
> `Legacy USB Support` should be set to `Auto`

> **Caution:**
> The `Install alongside` and `Replace partition` options are not 100% reliable and can cause the installation to fail.
>
> `Manual partitioning` is the **preferred** when installing CachyOS.

> **Tip:**
> It is highly recommended to restart the ISO after a failed installation attempt.
>
> Otherwise, continuous errors can happen during the installation process.
>
> This happens because the installer doesn't properly unmount partitions on a failed install.
>

<a id="installation-installation-on-root-installation-methods"></a>
### Installation Methods

<a id="installation-installation-on-root-manual-partitioning"></a>
#### Manual Partitioning

> **Note – Before proceeding with partitioning the disk for a UEFI installation.:**
> ```sh title='Execute this command in the terminal'
> efibootmgr -v
> ```
> If the output is: `EFI variables are not supported on this system.` Then the system is booted in Legacy/BIOS mode and you need to ensure that UEFI mode is configured in the BIOS/UEFI settings. Refer to **[Requisites section](#installation-installation-on-root-top).**

<a id="installation-installation-on-root-uefigpt"></a>
##### UEFI/GPT

The partition table for each boot manager varies. Please follow the correct instructions for each.

<a id="installation-installation-on-root-systemd-boot-refind"></a>
###### systemd-boot & rEFInd

1. Boot into the ISO and click the **Launch Installer** button

2. Set the preferred **Language** and **Region/Timezone**

3. Configure **Keyboard Layout**

4. Select **Manual partitioning**

5. Create a new partition with the following:
- ##### Size: **2048MiB**
- ##### Filesystem: **FAT32**
- ##### Mount point: **/boot**
- ##### Flags: **boot**

6. Create another partition for **root**:
- ##### Size: At least **20000MiB**
- ##### Filesystem: **Any**, refer [Filesystem](#installation-filesystem)
- ##### Mount point: **/**
- ##### Flags:

7. Double check that **Install boot loader on:** is pointing to **/boot**

8. Select the **Desktop Environment** of choice, see [Desktop Environments](#installation-desktop-environments).

9. Customize which packages should or should not be installed during the installation process.

10. Setup login credentials.

11. Review the installation summary on the Overview Page carefully. Proceed with the installation by clicking on **Install Now** if everything looks correct. Otherwise, go back and make any necessary changes.

<a id="installation-installation-on-root-limine"></a>
###### Limine

> **Note:**
> In storage space constrained environments, such as virtual machines, the /boot partition size can be reduced to 2048MiB.

1. Boot into the ISO and click the **Launch Installer** button

2. Set the preferred **Language** and **Region/Timezone**

3. Configure **Keyboard Layout**

4. Select **Manual partitioning**

5. Create a new partition with the following:
- ##### Size: **4096MiB**
- ##### Filesystem: **FAT32**
- ##### Mount point: **/boot**
- ##### Flags: **boot**

6. Create another partition for **root**:
- ##### Size: At least **20000MiB**
- ##### Filesystem: **Any**, refer [Filesystem](#installation-filesystem)
- ##### Mount point: **/**
- ##### Flags:

7. Double check that **Install boot loader on:** is pointing to **/boot**

8. Select the **Desktop Environment** of choice, see [Desktop Environments](#installation-desktop-environments).

9. Customize which packages should or should not be installed during the installation process.

10. Setup login credentials.

11. Review the installation summary on the Overview Page carefully. Proceed with the installation by clicking on **Install Now** if everything looks correct. Otherwise, go back and make any necessary changes.

<a id="installation-installation-on-root-grub"></a>
###### GRUB

1. Boot into the ISO and click the **Launch Installer** button

2. Set the preferred **Language** and **Region/Timezone**

3. Configure **Keyboard Layout**

4. Select **Manual partitioning**

5. Create a new partition with the following:
- ##### Size: At least **100MiB**
- ##### Filesystem: **FAT32**
- ##### Mount point: **/boot/efi**
- ##### Flags: **boot**

6. Create another partition for **root**:
- ##### Size: At least **20000MiB**
- ##### Filesystem: **Any**, refer [Filesystem](#installation-filesystem)
- ##### Mount point: **/**
- ##### Flags:

7. Double check that **Install boot loader on:** is pointing to **/boot/efi**

8. Select the **Desktop Environment** of choice, see [Desktop Environments](#installation-desktop-environments).

9. Customize which packages should or should not be installed during the installation process.

10. Setup login credentials.

11. Review the installation summary on the Overview Page carefully. Proceed with the installation by clicking on **Install Now** if everything looks correct. Otherwise, go back and make any necessary changes.

<a id="installation-installation-on-root-mbrbios"></a>
##### MBR/BIOS

<a id="installation-installation-on-root-grub"></a>
###### GRUB

1. Boot into the ISO and click the **Launch Installer** button

2. Set your preferred **Language** and **Region/Timezone**

3. Configure your **Keyboard Layout**

4. Select **Manual partitioning**

5. Create a new partition with the following:
- ##### Size: At least **20000MiB**
- ##### Filesystem: **Any**, refer [Filesystem](#installation-filesystem)
- ##### Mount point: **/**
- ##### Flags:

6. Double check that **Install boot loader on:** is pointing to your boot drive e.g: **/dev/sda**

7. Pick the **Desktop Environment** you'd like to use, see [Desktop Environments](#installation-desktop-environments).

8. Select the specific packages you wish to install from the provided list, and deselect any that you do not require.

9. Setup your login credentials.

10. Review the installation summary on the Overview Page carefully. If all the settings look correct for you, proceed with the installation by clicking on **Install Now**. Otherwise, go back and make any necessary changes.

<a id="installation-installation-on-root-limine"></a>
###### Limine

> **Note:**
> In storage space constrained environments, such as virtual machines, the /boot partition size can be reduced to 2048MiB.

1. Boot into the ISO and click the **Launch Installer** button

2. Set your preferred **Language** and **Region/Timezone**

3. Configure your **Keyboard Layout**

4. Select **Manual partitioning**

5. Create a new partition with the following:
- ##### Size: At least **4096MiB**
- ##### Filesystem: **FAT32**
- ##### Mount point: **/boot**
- ##### Flags: **boot**

6. Create another partition for **root**:
- ##### Size: At least **20000MiB**
- ##### Filesystem: **Any**, refer [Filesystem](#installation-filesystem)
- ##### Mount point: **/**
- ##### Flags:

7. Double check that **Install boot loader on:** is pointing to your boot drive e.g: **/dev/sda**

8. Pick the **Desktop Environment** you'd like to use, see [Desktop Environments](#installation-desktop-environments).

9. Select the specific packages you wish to install from the provided list, and deselect any that you do not require.

10. Setup your login credentials.

11. Review the installation summary on the Overview Page carefully. If all the settings look correct for you, proceed with the installation by clicking on **Install Now**. Otherwise, go back and make any necessary changes.

<a id="installation-installation-on-root-erase-disk"></a>
#### Erase Disk

The "Erase Disk" Option in Calamares will wipe the selected disk and install CachyOS to the target.

1. Boot into the ISO and click on **Launch Installer**

2. Select the preferred **Boot Manager**. Check the [Boot Managers](#installation-boot-managers) section for more information.

3. Set the preferred **Language** and **Region/Timezone**

4. Configure **Keyboard Layout**

5. Select **Erase Disk** and choose a [Filesystem](#installation-filesystem).

6. Select the **Desktop Environment** of choice, see [Desktop Environments](#installation-desktop-environments).

7. Customize which packages should or should not be installed during the installation process.

8. Setup login credentials.

9. Review the installation summary on the Overview Page carefully. Proceed with the installation by clicking on **Install Now** if everything looks correct. Otherwise, go back and make any necessary changes.

<a id="installation-installation-on-root-dual-booting-windows-and-cachyos"></a>
### Dual Booting Windows and CachyOS

> **Note – This guide assumes that Windows is already installed on the system and you decided to install CachyOS alongside it sharing the same drive.:**

> **Caution:**
> Dual booting Windows and Linux is not 100% reliable. Windows updates can break the bootloader by overwriting the EFI partition.
> In some cases issues might never occur, but for some users it can be a recurring problem.
>
> One way to avoid this issue is to install each operating system on separate drives.

- Prerequisites

- Disable Windows Fast Startup and Hibernation
- Open Windows Powershell as Administrator and execute the following command:
      ```ps
      powercfg /H off
      ```
Reboot the system to make sure the changes take effect.
- Windows BitLocker must be disabled
- Checking if BitLocker is enabled:
    ```ps title='Open a Command Prompt as administrator and execute the following command'
    manage-bde -status
    ```
  If Encryption Method shows as `None`, then BitLocker is disabled.
- Secure Boot must be disabled.
- A +30GB empty partition
- Guide on how to shrink a Windows partition:
- Press `Win + R`, type `diskmgmt.msc`, and press Enter to open Disk Management.
- Identify your main Windows partition (usually C:) and right-click on it.
- Click on `Shrink Volume...` and specify at least **30720MB** (30GB) and click on `Shrink`.
- Booteable USB with CachyOS
- Refer to the [Creating a Bootable CachyOS USB Drive](#installation-installation-prepare-creating-a-bootable-cachyos-usb-drive) section.

<a id="installation-installation-on-root-systemd-boot"></a>
###### systemd-boot

    **We need to copy the Windows EFI binaries to the Linux EFI partition so that the boot manager can recognize them.**

    
    1. Locate the **Windows EFI partition** with `lsblk`

            ```sh title='Execute this command in the terminal'
            lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT
            ```
            ```sh title='Example output'
                        NAME        FSTYPE   SIZE MOUNTPOINT
            zram0               15.3G [SWAP]
            nvme0n1            476.9G
            ├─nvme0n1p1 vfat     100M
            ├─nvme0n1p2           16M
            ├─nvme0n1p3 ntfs   234.4G
            ├─nvme0n1p4 ntfs     830M
            ├─nvme0n1p5 vfat       2G /boot
            └─nvme0n1p6 btrfs  239.6G /var/tmp
            ```
        EFI partitions are almost always formatted as `FAT32/vfat`. Since `nvme0n1p1` does not have a Linux mount point, we can assume that this partition is the Windows EFI partition.

    2. Temporarily mount the Windows EFI partition

            ```sh
            sudo mkdir /mnt/WinBoot
            sudo mount /dev/nvme0n1p1 /mnt/WinBoot # Replace `nvme0n1p1` with the name of the Windows EFI partition.
            ```

    3. Copy the EFI binaries from the **Windows EFI partition** to the **Linux EFI partition**:

            ```sh
            sudo cp -r /mnt/WinBoot/EFI/* /boot/EFI
            ```

    4. Unmount the previously mounted partition, and Windows should appear in the boot menu on the next startup.

            ```sh
            sudo umount /mnt/WinBoot
            sudo rm -r /mnt/WinBoot
            ```

    

<a id="installation-installation-on-root-grub"></a>
###### GRUB

    **GRUB uses os-prober to automatically detect the Windows EFI partition and add it to the boot menu.**

    
    1. Install and execute **os-prober**

            ```sh
            sudo pacman -S os-prober
            sudo os-prober
            ```

    2. Enable **os-prober** in the GRUB configuration file

            ```sh title='Press CTRL+S to save and CTRL+Q to exit from Micro'
            sudo micro /etc/default/grub
            # /etc/default/grub
            # Probing for other operating systems is disabled for security reasons. Read
            # documentation on GRUB_DISABLE_OS_PROBER, if still want to enable this
            # functionality install os-prober and uncomment to detect and include other
            # operating systems.
            GRUB_DISABLE_OS_PROBER=false

            sudo grub-mkconfig -o /boot/grub/grub.cfg
            ```

        **Windows should now be added to the boot menu.**
