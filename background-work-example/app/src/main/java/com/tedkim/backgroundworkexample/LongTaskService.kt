package com.tedkim.backgroundworkexample

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.util.Log
import android.widget.Toast
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class LongTaskService : Service() {

    companion object {
        private const val TAG = "LongTaskService"
    }

    private val serviceScope = CoroutineScope(Dispatchers.Main)

    override fun onCreate() {
        super.onCreate()

        Log.i(TAG, "LongTaskService.onCreate()")
        Toast.makeText(this, "LongTaskService.onCreate()", Toast.LENGTH_SHORT).show()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        serviceScope.launch {
            startLongTask()
            Log.i(TAG, "LongTaskService.startLongTask()")
            Toast.makeText(this@LongTaskService, "LongTaskService.startLongTask()", Toast.LENGTH_SHORT).show()
            stopSelf()
        }
        return START_NOT_STICKY
    }

    private suspend fun startLongTask() {
        withContext(Dispatchers.IO) {
            delay(5000)
        }
    }

    override fun onBind(intent: Intent): IBinder? {
        return null
    }

    override fun onDestroy() {
        Log.i(TAG, "LongTaskService.onDestroy()")
        Toast.makeText(this, "LongTaskService.onDestroy()", Toast.LENGTH_SHORT).show()
    }
}