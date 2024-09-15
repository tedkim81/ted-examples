package com.tedkim.launchmodetester

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Build
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.tedkim.launchmodetester.databinding.ActivityBaseBinding

abstract class BaseActivity : AppCompatActivity() {

    private lateinit var binding: ActivityBaseBinding
    private var onNewIntentCnt = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityBaseBinding.inflate(layoutInflater)
        setContentView(binding.root)
        initViews()
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)

        @SuppressLint("SetTextI18n")
        binding.activityName.text = "${javaClass.simpleName}(onNewIntent: ${++onNewIntentCnt})"
    }

    private fun initViews() {
        binding.activityName.text = javaClass.simpleName

        val buttonActivityMap = mapOf(
            binding.btnStandard to StandardActivity::class.java,
            binding.btnStandardWithAffinity to StandardWithAffinityActivity::class.java,
            binding.btnSingleTop to SingleTopActivity::class.java,
            binding.btnSingleTask to SingleTaskActivity::class.java,
            binding.btnSingleTaskWithAffinity to SingleTaskWithAffinityActivity::class.java,
            binding.btnSingleInstance to SingleInstanceActivity::class.java,
            binding.btnSingleInstanceWithAffinity to SingleInstanceWithAffinityActivity::class.java,
            binding.btnSingleInstancePerTask to SingleInstancePerTaskActivity::class.java,
            binding.btnSingleInstancePerTaskWithAffinity to SingleInstancePerTaskWithAffinityActivity::class.java,
        )

        buttonActivityMap.forEach { (button, activity) ->
            button.setOnClickListener {
                startActivityWithFlags(activity)
            }
        }
    }

    private fun startActivityWithFlags(activity: Class<*>) {
        val intent = Intent(this, activity)
        val checkBoxFlagMap = mutableMapOf(
            binding.checkBoxBroughtToFront to Intent.FLAG_ACTIVITY_BROUGHT_TO_FRONT,
            binding.checkBoxClearTask to Intent.FLAG_ACTIVITY_CLEAR_TASK,
            binding.checkBoxClearTop to Intent.FLAG_ACTIVITY_CLEAR_TOP,
            binding.checkBoxExcludeFromRecents to Intent.FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS,
            binding.checkBoxForwardResult to Intent.FLAG_ACTIVITY_FORWARD_RESULT,
            binding.checkBoxLaunchedFromHistory to Intent.FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY,
            binding.checkBoxLaunchAdjacent to Intent.FLAG_ACTIVITY_LAUNCH_ADJACENT,
            binding.checkBoxMultipleTask to Intent.FLAG_ACTIVITY_MULTIPLE_TASK,
            binding.checkBoxNewDocument to Intent.FLAG_ACTIVITY_NEW_DOCUMENT,
            binding.checkBoxNewTask to Intent.FLAG_ACTIVITY_NEW_TASK,
            binding.checkBoxNoAnimation to Intent.FLAG_ACTIVITY_NO_ANIMATION,
            binding.checkBoxNoHistory to Intent.FLAG_ACTIVITY_NO_HISTORY,
            binding.checkBoxNoUserAction to Intent.FLAG_ACTIVITY_NO_USER_ACTION,
            binding.checkBoxPreviousIsTop to Intent.FLAG_ACTIVITY_PREVIOUS_IS_TOP,
            binding.checkBoxReorderToFront to Intent.FLAG_ACTIVITY_REORDER_TO_FRONT,
            binding.checkBoxResetTaskIfNeeded to Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED,
            binding.checkBoxRetainInRecents to Intent.FLAG_ACTIVITY_RETAIN_IN_RECENTS,
            binding.checkBoxSingleTop to Intent.FLAG_ACTIVITY_SINGLE_TOP,
            binding.checkBoxTaskOnHome to Intent.FLAG_ACTIVITY_TASK_ON_HOME,
        )
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
            checkBoxFlagMap[binding.checkBoxMatchExternal] = Intent.FLAG_ACTIVITY_MATCH_EXTERNAL
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            checkBoxFlagMap[binding.checkBoxRequireDefault] = Intent.FLAG_ACTIVITY_REQUIRE_DEFAULT
            checkBoxFlagMap[binding.checkBoxRequireNonBrowser] = Intent.FLAG_ACTIVITY_REQUIRE_NON_BROWSER
        }
        checkBoxFlagMap.forEach { (checkBox, flag) ->
            if (checkBox.isChecked) {
                intent.addFlags(flag)
            }
        }
        startActivity(intent)
    }
}