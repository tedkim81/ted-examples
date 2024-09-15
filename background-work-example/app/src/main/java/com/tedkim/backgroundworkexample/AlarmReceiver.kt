package com.tedkim.backgroundworkexample

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.os.Build
import android.util.Log

class AlarmReceiver : BroadcastReceiver() {

    companion object {
        private const val TAG = "AlarmReceiver"
    }

    override fun onReceive(context: Context, intent: Intent) {
        Log.i(TAG, "AlarmReceiver.onReceive()")
        try {
            context.startService(Intent(context, LongTaskService::class.java))
        } catch (e: Exception) {
            // 앱이 종료된 상태에서 startService 호출하면 android.app.BackgroundServiceStartNotAllowedException 발생
            Log.e(TAG, "startService error: $e", e)
        }
    }
}