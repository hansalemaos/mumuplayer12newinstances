# Creates new instances of MuMu Player 12 with a copy of the entire system disk.

### Tested against Windows 10 / Python 3.11 / Anaconda

### pip install mumuplayer12newinstances


```python
# Install MuMu Player 12

from mumuplayer12newinstances import clone_mumu_instance

newfol = clone_mumu_instance(
    vm_config={
        "vm": {
            "cpu": "4",
            "memory": "6",
            "phone": {
                "brand": "XiaoMi",
                "imei": "861151054342984",
                "manufacturer": "XiaoMi",
                "miit": "Redmi Note 8 Pro",
                "model": "Redmi Note 8 Pro",
                "number": "",
            },
            "root": "true",
        }
    },
    shell_config={
        "player": {
            "advanced": {"show_fps": {"enabled": "false"}},
            "rotation": {"mode": "auto"},
        },
        "renderer": {
            "advanced": {
                "hight_fps": {"enabled": "true", "input": "1"},
                "light": {"enabled": "true", "input": "50"},
                "style": {"enabled": "true", "input": "none"},
            },
            "audio_out_hardware_off": "1",
            "force_dedicated_gpu": "true",
            "fps_limit": "30",
            "fps_limit_low": "15",
            "fps_limit_real": "60",
            "opt_flag": {"texture_policy": "0"},
            "platform": "vk",
            "present_vsync_on": "0",
            "resolution": {
                "dpi": "240.000000",
                "height": "900.000000",
                "width": "1600.000000",
            },
        },
    },
    customer_config={
        "customer": {
            "apk_associate": "true",
            "app_keptlive": "false",
            "joystick_function": "true",
            "pc_sleep": "true",
            "quit_directly": "false",
            "run_limitation": "false",
        },
        "setting": {
            "disk_share": {"mode": {"choose": "disk_share.mode.writable"}},
            "environment": {
                "cpu": {"best": "4", "max": "6"},
                "memory": {"best": "6", "max": "16"},
                "screen": {"dpr": "1.000000", "height": "1080", "width": "1920"},
            },
            "frame_setting": {
                "desired_framerate": "60",
                "display_framerate": "0",
                "dynamic_adjust_framerate": "0",
                "fps_limit_low": "15",
                "max_frame_rate_limit": "240",
                "vertical_sync": "0",
            },
            "level": {
                "user": {
                    "computer": "middle",
                    "cpu": "middle",
                    "gpu": "high",
                    "memory": "high",
                }
            },
            "other_optimization": {"separate_graphics_card": "1"},
            "other_setting": {
                "apk_association": "1",
                "app_keptlive": "0",
                "joystick_function": "1",
                "pc_sleep": "1",
                "quit_setting": {
                    "mode": {"choose": "other_setting.quit_setting.mode.popupconfirm"}
                },
                "root_mode": "1",
                "run_limitation": "0",
                "use_system_default_mouse": "1",
            },
            "performance": {
                "mode": {
                    "choose": "performance.mode.middle",
                    "custom": {"cpu": "4", "memory": "6.000000"},
                    "high": {"cpu": "6", "memory": "12"},
                    "low": {"cpu": "1", "memory": "1"},
                    "middle": {"cpu": "4", "memory": "6"},
                }
            },
            "phone": {
                "brand": "XiaoMi",
                "imei": "861151054342984",
                "manufacturer": "XiaoMi",
                "miit": "Redmi Note 8 Pro",
                "mode": {"choose": "phone.mode.preset"},
                "model": "Redmi Note 8 Pro",
                "number": "",
            },
            "player": {"window": {"remember": "0"}},
            "record": {"time": {"first": "0"}},
            "render": {
                "avalibale": {"directx": "1", "vulkan": "1"},
                "mode": {
                    "choose": "render.mode.highperformance",
                    "highperformance": "Vulkan",
                },
            },
            "resolution": {
                "current": "1600.000000:900.000000:240.000000",
                "mode": {
                    "choose": "resolution.mode.tablet",
                    "custom": "1600.000000:900.000000:240.000000",
                    "intelligence": "1600:900:240",
                    "intelligence_enable": "0",
                    "intelligence_preselect_enable": "1",
                    "phone": "0.000000:0.000000:0.000000",
                    "tablet": "1600.000000:900.000000:240.000000",
                    "widescreen": "0.000000:0.000000:0.000000",
                },
            },
            "rotation_setting": {"mode": {"choose": "rotation_setting.mode.auto"}},
            "screen_setting": {
                "brightness": "50",
                "max_brightness": "100",
                "style": {"choose": "screen_setting.style.common"},
            },
            "shortcut": {
                "automute": "1",
                "disable_zoom_screen": "1",
                "enable_esc_as_quit_full_screen": "1",
                "enable_switch_tab_to_target": "0",
                "keys": {
                    "apk_install": {"conflict": "0", "text": "null"},
                    "boss_key": {"conflict": "0", "text": "Alt+Q"},
                    "file_transfer": {"conflict": "0", "text": "null"},
                    "full_screen_mode": {"conflict": "0", "text": "F11"},
                    "game_tools": {"conflict": "0", "text": "null"},
                    "go_home": {"conflict": "0", "text": "Home"},
                    "gps": {"conflict": "0", "text": "null"},
                    "joystick": {"conflict": "0", "text": "null"},
                    "keymap": {"conflict": "0", "text": "null"},
                    "keymap_config_next": {"conflict": "0", "text": "Ctrl+]"},
                    "keymap_config_previous": {"conflict": "0", "text": "Ctrl+["},
                    "keymap_tip": {"conflict": "0", "text": "F12"},
                    "lock_screen": {"conflict": "0", "text": "null"},
                    "mini_mode": {"conflict": "0", "text": "Alt+G"},
                    "multi_player": {"conflict": "0", "text": "null"},
                    "mute": {"conflict": "0", "text": "Ctrl+0"},
                    "operate_record": {"conflict": "0", "text": "null"},
                    "overseas_acceleration": {"conflict": "0", "text": "null"},
                    "pause_or_continue_operate_record": {
                        "conflict": "0",
                        "text": "null",
                    },
                    "pause_or_continue_operate_script": {
                        "conflict": "0",
                        "text": "null",
                    },
                    "pause_or_continue_screen_record": {
                        "conflict": "0",
                        "text": "null",
                    },
                    "pause_or_continue_sync": {"conflict": "0", "text": "null"},
                    "return_back": {"conflict": "0", "text": "Esc"},
                    "screen_record": {"conflict": "0", "text": "null"},
                    "screenshot": {"conflict": "0", "has_modify": "1", "text": "F9"},
                    "scroll_screen": {"conflict": "0", "text": "null"},
                    "shake": {"conflict": "0", "text": "null"},
                    "start_or_end_operate_record": {"conflict": "0", "text": "null"},
                    "start_or_end_screen_record": {"conflict": "0", "text": "null"},
                    "start_or_end_sync": {"conflict": "0", "text": "null"},
                    "stop_operate_record_script": {"conflict": "0", "text": "null"},
                    "switch_tab": {"conflict": "0", "text": "Ctrl+Tab"},
                    "switch_to_target_tab": {"conflict": "0", "text": "Ctrl+1~9"},
                    "volume_turn_down": {"conflict": "0", "text": "Ctrl+Down"},
                    "volume_turn_up": {"conflict": "0", "text": "Ctrl+Up"},
                    "window_top": {"conflict": "0", "text": "null"},
                    "zoom_in_screen": {"conflict": "0", "text": "null"},
                    "zoom_out_screen": {"conflict": "0", "text": "null"},
                    "zoom_screen": {"conflict": "0", "text": "Ctrl+mouse wheel"},
                },
                "mouse_right_btn_as_return_back": "0",
            },
            "ui_setting": {"mode": {"choose": "ui_setting.mode.hideallui"}},
            "video_memory": {"strategy": {"choose": "video_memory.strategy.auto"}},
            "volume_setting": {
                "loudspeaker": "",
                "microphone": "",
                "system_volume": {"close": "1", "max": "0"},
            },
        },
    },
    basefolder_vms=r"C:\Program Files\Netease\MuMuPlayerGlobal-12.0\vms",
    vboxmanage_path=r"C:\Program Files\MuMuVMMVbox\Hypervisor\MuMuVMMManage.exe",
)
print(newfol)

```