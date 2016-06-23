# andsdk-files-for-ccc
本项目是为了便于在 CocosCreator 项目中集成 AnySDK 而创建。

##更新日志
1. 2016-6-23 update AnySDK files for CocosCreator 1.1.1


##使用步骤

###下载 andsdk-files-for-ccc 项目

```
$ cd youdir
$ git clone https://github.com/eddy2015/anysdk-files-for-ccc
```
###拷贝 AnySDK 文件到 CocosCreator 项目
该步骤需要安装 Python，并配置好环境变量。copy-anysdk-files.py 脚本会把 andsdk-files-for-ccc/build 目录下的所有文件**拷贝覆盖**到 CocosCreator 项目中。

当然你也可以手动拷贝，拷贝到项目中对应的目录即可。

python copy-anysdk-files.py +你的 CocosCreator 项目路径。
如下：

```
$ cd youdir/andsdk-files-for-ccc
$ python copy-anysdk-files.py /Users/eddy/Documents/CocosCreatorGitHub/testanysdk/
```

###拷贝覆盖文件引起的一些问题
拷贝拷贝覆盖 AnySDK 文件到 CocosCreator 项目中，会覆盖掉一些原来你改动过的文件。假如你的项目使用了 git 管理，那么你就很容易找到被 copy-anysdk-files.py 脚本添加或改动过的文件了。

下面列出一些常见需要手动恢复的文件：

例如 build/jsb-default/frameworks/runtime-src/proj.android/AndroidManifest.xml 文件中的 Android APK 包名被改动了，你需要手动修改回原来的包名。其他文件一般不需要手动修复，但或许你改动了 AppActivity.java 文件也是比较常见的。

如下图：
![e5fc1e3970bd88c2fdbe762236273989.png](http://moefq.com/images/2016/06/23/e5fc1e3970bd88c2fdbe762236273989.png)

copy-anysdk-files.py 改动的文件如下：

```
build/jsb-default/frameworks/cocos2d-x/cocos/scripting/js-bindings/script/jsb.js
build/jsb-default/frameworks/runtime-src/Classes/AppDelegate.cpp
build/jsb-default/frameworks/runtime-src/proj.android/AndroidManifest.xml
build/jsb-default/frameworks/runtime-src/proj.android/build-cfg.json
build/jsb-default/frameworks/runtime-src/proj.android/jni/Android.mk
build/jsb-default/frameworks/runtime-src/proj.android/jni/hellojavascript/main.cpp
build/jsb-default/frameworks/runtime-src/proj.android/src/org/cocos2dx/javascript/AppActivity.java
```
copy-anysdk-files.py 增加的文件如下：

```
build/jsb-default/frameworks/cocos2d-x/anysdk/src/jsb_anysdk.js
build/jsb-default/frameworks/cocos2d-x/anysdk/src/jsb_anysdk_constants.js
build/jsb-default/frameworks/runtime-src/Classes/jsb_anysdk_basic_conversions.cpp
build/jsb-default/frameworks/runtime-src/Classes/jsb_anysdk_basic_conversions.h
build/jsb-default/frameworks/runtime-src/Classes/jsb_anysdk_protocols_auto.cpp
build/jsb-default/frameworks/runtime-src/Classes/jsb_anysdk_protocols_auto.hpp
build/jsb-default/frameworks/runtime-src/Classes/manualanysdkbindings.cpp
build/jsb-default/frameworks/runtime-src/Classes/manualanysdkbindings.hpp
build/jsb-default/frameworks/runtime-src/proj.android/libs/libPluginProtocol.jar
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/Android.mk
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/PluginJavaData.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/PluginJniHelper.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/PluginJniMacros.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/PluginUtils.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/Statistics.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/lib/arm64-v8a/libPluginProtocolStatic.a
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/lib/armeabi/libPluginProtocolStatic.a
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/lib/armeabi-v7a/libPluginProtocolStatic.a
build/jsb-default/frameworks/runtime-src/proj.android/protocols/android/lib/x86/libPluginProtocolStatic.a
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/AgentManager.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/JSBRelation.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/PluginFactory.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/PluginManager.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/PluginParam.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/PluginProtocol.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolAds.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolAnalytics.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolCrash.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolCustom.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolIAP.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolPush.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolREC.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolShare.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolSocial.h
build/jsb-default/frameworks/runtime-src/proj.android/protocols/include/ProtocolUser.h
build/jsb-default/frameworks/runtime-src/proj.android/res/drawable/plugin_btn_close.png
build/jsb-default/frameworks/runtime-src/proj.android/res/drawable/plugin_ui_ad.png
build/jsb-default/frameworks/runtime-src/proj.android/res/layout/plugin_ads.xml
build/jsb-default/frameworks/runtime-src/proj.android/res/layout/plugin_login.xml
build/jsb-default/frameworks/runtime-src/proj.android/res/values/plugin_string.xml
build/jsb-default/frameworks/runtime-src/proj.android/res/values-en/plugin_string.xml
```


