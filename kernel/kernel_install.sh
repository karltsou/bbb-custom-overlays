#/bin/base

kernel_version=$(cat ./kernel_version)
user=$(whoami)
echo Current kernel version is $kernel_version
echo Check installation path /media/$user/rootfs/boot/

if [ ! -d "/media/$user/rootfs/boot" ]
then
	echo "Missing path"
	exit 0
else
	echo "OK"
fi

echo Preparing images ...
if [ ! -f "./deploy/$kernel_version.zImage" ] 
then
	echo Missing $kernel_version.zImage
	exit 0
else
	echo Install $kernel_version.zImage dtbs and modules
	sudo cp -v ./deploy/${kernel_version}.zImage /media/$user/rootfs/boot/vmlinuz-${kernel_version}
	sudo mkdir -p /media/$user/rootfs/boot/dtbs/${kernel_version}/
	sudo tar xfv ./deploy/${kernel_version}-dtbs.tar.gz -C /media/$user/rootfs/boot/dtbs/${kernel_version}/
	sudo tar xfv ./deploy/${kernel_version}-modules.tar.gz -C /media/$user/rootfs/
	sudo sed -i 's/uame_r=.*/uname_r=${kernel_version}/g' /media/$user/rootfs/boot/uEnv.txt"
fi

echo Done!
