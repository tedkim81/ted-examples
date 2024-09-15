package com.tedkim.backgroundworkexample

import android.app.AlarmManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import android.os.Bundle
import android.os.SystemClock
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.lifecycle.lifecycleScope
import com.tedkim.backgroundworkexample.databinding.ActivityMainBinding
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlin.system.exitProcess

class MainActivity : AppCompatActivity() {

    companion object {
        const val PERMISSION_REQUEST_CODE = 1
    }

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        initViews()
    }

    private fun initViews() {
        binding.btnCoroutineExample.setOnClickListener {
            startCoroutineExample()
        }
        binding.btnServiceExample.setOnClickListener {
            startServiceExample()
        }
        binding.btnServiceWhenTerminated.setOnClickListener {
            terminateAndStartService()
        }
        binding.btnForegroundServiceExample.setOnClickListener {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU && ContextCompat.checkSelfPermission(this, android.Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) {
                ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.POST_NOTIFICATIONS), PERMISSION_REQUEST_CODE)
            } else {
                startForegroundServiceExample()
            }
        }
    }

    private fun startCoroutineExample() {
        lifecycleScope.launch {
            delay(3000)
            Toast.makeText(this@MainActivity, "Coroutine example after delay", Toast.LENGTH_SHORT).show()
        }
        Toast.makeText(this, "Coroutine example before delay", Toast.LENGTH_SHORT).show()
    }

    private fun startServiceExample() {
        startService(Intent(this, LongTaskService::class.java))
    }

    private fun terminateAndStartService() {
        val alarmManager = getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val intent = Intent(this, AlarmReceiver::class.java)
        val pendingIntent = PendingIntent.getBroadcast(this, 0, intent, PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
        val triggerAtTime = SystemClock.elapsedRealtime() + 5000L
        alarmManager.set(AlarmManager.ELAPSED_REALTIME_WAKEUP, triggerAtTime, pendingIntent)

        finish()
        exitProcess(0)
    }

    private fun startForegroundServiceExample() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            startForegroundService(Intent(this, ForegroundService::class.java))
        }
    }
}