--- setup.py.orig	2021-07-06 07:49:28 UTC
+++ setup.py
@@ -46,7 +46,7 @@ REQUIRES = [
     "PyJWT==1.7.1",
     # PyJWT has loose dependency. We want the latest one.
     "cryptography==3.3.2",
-    "pip>=8.0.3,<20.3",
+    "pip>=8.0.3",
     "python-slugify==4.0.1",
     "pyyaml==5.4.1",
     "requests==2.25.1",
