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





