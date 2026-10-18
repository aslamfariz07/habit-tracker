HABIT TRACKER - Android APK builder
===================================

You do not need Android Studio. GitHub builds the APK for you, free.

1. Create a free account at github.com and make a new repository
   (any name, Public or Private).
2. Upload everything in this folder to the repository root:
   "Add file" > "Upload files", then drag in package.json,
   capacitor.config.json, README.txt, the www folder, the scripts folder
   and the .github folder.
   (If the .github folder does not upload, use "Add file" > "Create new file",
   type  .github/workflows/build-apk.yml  as the name, and paste in the
   contents of that file.)
3. Open the "Actions" tab. Choose "Build Android APK" and click
   "Run workflow". If it already started on its own, just wait.
4. After about 5-8 minutes, open the finished run and download the
   "habit-tracker-apk" file at the bottom. Unzip it to get app-debug.apk.
5. Copy app-debug.apk to your phone and open it. Allow "Install unknown apps"
   for your Files app or browser when asked. Android may show a
   "Play Protect" notice for an app not from the Play Store; choose
   "Install anyway".

Your data
  The app stores everything in its own private storage on the phone and
  works fully offline. Updating by installing a newer APK over the old one
  keeps your data. Uninstalling the app deletes it, so use the in-app
  Backup (cloud icon on the Habits tab) first.

Notes
  - This is a debug-signed APK, fine for your own phone. Publishing to the
    Play Store needs a release-signed build.
  - Reminder times are saved and shown in the Plan tab. They do not trigger
    notifications while the app is closed.
  - Build it on your own computer instead: install Node 18+, JDK 17 and
    Android Studio, then run
        npm install
        npx cap add android
        python3 scripts/set-icons.py   (optional, needs: pip install pillow)
        npx cap sync android
        cd android && ./gradlew assembleDebug
    The APK is at android/app/build/outputs/apk/debug/app-debug.apk
