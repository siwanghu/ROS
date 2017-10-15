### Turtlebot学习笔记 create by siwanghu v1.0
# ROS安装  
## ubuntu14.04上安装ROS Indigo版本
> **设置安装软件源**  
> sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'  
>  
> **设置key**  
> sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116  
>  
> **安装**  
> sudo apt-get update  
> sudo apt-get install ros-indigo-desktop-full
>  
> **初始化rosdep**  
> sudo rosdep init  
> rosdep update  
>  
> **初始化ROS开发环境**  
> echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc  
> source ~/.bashrc  
>  
> **安装ROS工具包**  
> sudo apt-get install python-rosinstall
  
# Turtlebot包安装  
## 安装ROS Indigo对应的Turtlebot包 
> **ubuntu软件安装源更新**  
> sudo apt-get update  
>
> **Turtlebot包安装**  
> sudo apt-get install ros-indigo-turtlebot ros-indigo-turtlebot-apps ros-indigo-turtlebot-interactions ros-indigo-turtlebot-simulator ros-indigo-kobuki-ftdi ros-indigo-rocon-remocon ros-indigo-rocon-qt-library ros-indigo-ar-track-alvar-msgs  
# Turtlebot测试
> **启动ROS**  
> roscore  
>  
> **设备驱动配置**  
> 使用 ls /dev/kobuki命令，如果没有显示对应的设备驱动 **/dev/kobuki** 则使用命令 **rosrun kobuki_ftdi create_udev_rules** 添加，重启Turtlebot底盘即可  
>  
> **键盘控制底盘**  
> roslaunch turtlebot_bringup minimal.launch  
> roslaunch turtlebot_teleop keyboard_teleop.launch  
>  
> **通过发布主题命令控制底盘**  
> rostopic pub -r 10 /cmd_vel_mux/input/navi  geometry_msgs/Twist  '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'  
# Kinect配置  
> **安装驱动**  
> sudo apt-get install ros-indigo-openni-* ros-indigo-openni2-* ros-indigo-freenect-*  
> rospack profile  
>  
> **设置环境变量(非常重要,做任何事之前都要查看和配置)**  
> echo $TURTLEBOT_3D_SENSOR  
> 如果输出的不是kinect则需要重新配置  
>  
> **如果你看到一个3D传感器，例如asus_xtion_pro，您将需要设置环境变量的默认值，修改和重新启动终端：**  
> echo "export TURTLEBOT_3D_SENSOR=kinect" >> .bashrc  
# Kinect测试  
> **启动turtlebot**  
> roslaunch turtlebot_bringup minimal.launch  
>  
> **启动Kinect**  
> roslaunch freenect_launch freenect-registered-xyzrgb.launch （Kinect新版本）  
> roslaunch openni_launch openni.launch (Kinect或旧版本)  
> **针对Asus Xtion, Xtion Pro, or Primesense 1.08/1.09 cameras:**  
> roslaunch openni2_launch openni2.launch depth_registration:=true  
>  + 图片 rosrun image_view image_view image:=/camera/rgb/image_color  
> + 深度图 rosrun image_view image_view image:=/camera/depth_registered/image  
>
> **在RVIZ上查看相机**  
> roslaunch turtlebot_bringup 3dsensor.launch  
> roslaunch turtlebot_rviz_launchers view_robot.launch  
# Turtlebot跟随  
> **启动Turtlebot**  
> roslaunch turtlebot_bringup minimal.launch  
>  
> **启动跟随脚本**  
> roslaunch turtlebot_follower follower.launch  
# Turtlebot建图导航  
## 创建地图 
>  
> **启动Turtlebot** *roslaunch turtlebot_bringup minimal.launch*  
>   
> **创建地图** *roslaunch turtlebot_navigation gmapping_demo.launch*  
>  
> **打开rviz** *roslaunch turtlebot_rviz_launchers view_navigation.launch*  
>  
> **手动扫描建图** *roslaunch turtlebot_teleop keyboard_teleop.launch*  
>  
> **保存地图** *rosrun map_server map_saver -f /tmp/my_map*  
## 自主导航  
> **启动Turtlebot** *roslaunch turtlebot_bringup minimal.launch*  
>  
> **启动导航模块** *roslaunch turtlebot_navigation amcl_demo.launch map_file:=/tmp/my_map.yaml*  
>  
> 导航模块有时启动失败可以使用这种方式启动(**非常重要**)  
> export TURTLEBOT_MAP_FILE=～/tmp/my_map.yaml  
> roslaunch turtlebot_navigation amcl_demo.launch  
>  
> **打开rviz** *roslaunch turtlebot_rviz_launchers view_navigation.launch --screen*  
>  
> **当启动之后，TurtleBot并不知道自己在哪个位置,需要给它提供它在地图上的位置：**  
> + 点击rviz中的”2D Pose Estimate”按钮
> + 在地图上标出TurtleBot的近似位置，并指出TurtleBot的朝向（TurtleBot的正运动方向)  
> + 点击rviz上的”2D Nav Goal”按钮  
> + 在地图上标出TurtleBot的导航目标，并且指出其在导航终点的朝向  
# 网络配置  
> 主机也需要和笔记本一样安装ROS和Turtlebot包(**参考上面ROS与Turtlebot包安装过程**)  
>  
> 主机与笔记本需要同步时钟，在主机与笔记本上都需要安装chrony(**非常重要**)  
> sudo apt-get install chrony  
> sudo ntpdate ntp.ubuntu.com  
>  
> 在主机和笔记本电脑上都需要安装ssh-server  
> sudo apt-get install openssh-server  
>  
> 在笔记本电脑端配置  
> echo export ROS_MASTER_URI=http://localhost:11311 >> ~/.bashrc  
> echo export ROS_HOSTNAME=**笔记本电脑IP地址** >> ~/.bashrc  
>  
> 在主机端配置  
> echo export ROS_MASTER_URI=http://**笔记本电脑IP地址**:11311 >> ~/.bashrc  
> echo export ROS_HOSTNAME=**主机IP地址** >> ~/.bashrc  
## 网络测试  
> 主机开启一个终端使用ssh命令登陆笔记本电脑  
> ssh username@ip  
> 运行roscore  
>  
> 主机在开启一个终端使用ssh命令登陆笔记本电脑  
> ssh username@ip  
> 运行roslaunch turtlebot_bringup minimal.launch  
>  
> 在主机开启一个终端  
> 运行roslaunch turtlebot_teleop keyboard_teleop.launch  
> 如果在主机端可以操作Turtlebot,说明网络配置成功  









