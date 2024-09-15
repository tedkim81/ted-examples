package com.tedkim.backgroundworkexample

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.content.Intent
import android.os.Build
import android.os.IBinder
import android.util.Log
import android.widget.Toast
import androidx.core.app.NotificationCompat
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext


class ForegroundService : Service() {

    companion object {
        private const val TAG = "ForegroundService"
        private const val CHANNEL_ID = "ForegroundServiceChannel"
    }

    private val serviceScope = CoroutineScope(Dispatchers.Main)

    override fun onCreate() {
        super.onCreate()

        Log.i(TAG, "ForegroundService.onCreate()")
        Toast.makeText(this, "ForegroundService.onCreate()", Toast.LENGTH_SHORT).show()

        createNotificationChannel()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Example Foreground Service")
            .setContentText("This is running in the foreground")
            .setSmallIcon(R.drawable.ic_notification)
            .build()
        startForeground(1, notification)

        serviceScope.launch {
            startLongTask()
            Log.i(TAG, "ForegroundService.startLongTask()")
            Toast.makeText(this@ForegroundService, "ForegroundService.startLongTask()", Toast.LENGTH_SHORT).show()
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
        Log.i(TAG, "ForegroundService.onDestroy()")
        Toast.makeText(this, "ForegroundService.onDestroy()", Toast.LENGTH_SHORT).show()
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val serviceChannel = NotificationChannel(
                CHANNEL_ID,
                "Foreground Service Channel",
                NotificationManager.IMPORTANCE_HIGH
            )
            val manager = getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(serviceChannel)
        }
    }
}