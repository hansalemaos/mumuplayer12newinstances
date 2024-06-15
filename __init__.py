from list_all_files_recursively_short import (
    get_folder_file_complete_path,
    get_short_path_name_cached,
)
import ast
import subprocess
import os
import shutil
import re
from flatten_any_dict_iterable_or_whatsoever import (
    fla_tu,
    set_in_original_iter,
)
import xmltodict
from killallappsinfolder import ProcKiller
from time import sleep
from typing import Union

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
creationflags = subprocess.CREATE_NO_WINDOW
invisibledict = {
    "startupinfo": startupinfo,
    "creationflags": creationflags,
    "start_new_session": True,
}

regex_for_uuid = re.compile(
    r"[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}", flags=re.IGNORECASE
)


def clone_mumu_instance(
    vm_config: Union[dict, None] = None,
    shell_config: Union[dict, None] = None,
    customer_config: Union[dict, None] = None,
    basefolder_vms: str = r"C:\Program Files\Netease\MuMuPlayerGlobal-12.0\vms",
    vboxmanage_path: str = r"C:\Program Files\MuMuVMMVbox\Hypervisor\MuMuVMMManage.exe",
) -> str:
    r"""
        Clones a MuMu instance (with entire system disk).

        :param vm_config: A dictionary containing the configuration for the virtual machine. Defaults to None.
        :type vm_config: Union[dict, None], optional
        :param shell_config: A dictionary containing the configuration for the shell. Defaults to None.
        :type shell_config: Union[dict, None], optional
        :param customer_config: A dictionary containing the configuration for the customer. Defaults to None.
        :type customer_config: Union[dict, None], optional
        :param basefolder_vms: The base folder for the virtual machines. Defaults to r"C:\Program Files\Netease\MuMuPlayerGlobal-12.0\vms".
        :type basefolder_vms: str, optional
        :param vboxmanage_path: The path to the VirtualBox manage executable. Defaults to r"C:\Program Files\MuMuVMMVbox\Hypervisor\MuMuVMMManage.exe".
        :type vboxmanage_path: str, optional
        :return: The path to the newly created folder.
        :rtype: str

        :Example:
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

    """

    if not vm_config:
        vm_config = {
            "vm": {
                "cpu": "4",
                "ginstance": "",
                "memory": "6",
                "nat": {
                    "port_forward": {
                        "adb": {"host_port": "16928"},
                        "api": {"host_port": "17979"},
                        "event": {"host_port": "20025"},
                        "frontend": {"host_port": "24096"},
                        "gateway": {"host_port": "25120"},
                        "input": {"host_port": "19002"},
                    }
                },
                "phone": {
                    "brand": "Samsung",
                    "imei": "867672051170619",
                    "manufacturer": "Samsung",
                    "miit": "SM-A536E",
                    "model": "Galaxy A53 5G",
                    "number": "",
                },
                "root": "true",
                "system_vdi": {"sharable": "Writable"},
            }
        }

    if not shell_config:
        shell_config = {
            "player": {
                "advanced": {"show_fps": {"enabled": "false"}},
                "rotation": {"mode": "auto"},
                "uu_remote": {"should_show": "false"},
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
                "opt_flag": {"texture_policy": "1"},
                "platform": "vk",
                "present_vsync_on": "0",
                "resolution": {
                    "dpi": "320.000000",
                    "height": "1600.000000",
                    "width": "900.000000",
                },
            },
        }

    if not customer_config:
        customer_config = {
            "customer": {
                "apk_associate": "false",
                "app_keptlive": "false",
                "default_location_latitute": "-15.783333333333",
                "default_location_longtitute": "-47.933333333333",
                "joystick_function": "false",
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
                    "joystick_function": "0",
                    "pc_sleep": "1",
                    "quit_setting": {
                        "mode": {
                            "choose": "other_setting.quit_setting.mode.popupconfirm"
                        }
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
                    "brand": "Samsung",
                    "imei": "867672051170619",
                    "manufacturer": "Samsung",
                    "miit": "SM-A536E",
                    "mode": {"choose": "phone.mode.preset"},
                    "model": "Galaxy A53 5G",
                    "number": "",
                },
                "player": {
                    "window": {
                        "fullscreen": "0",
                        "height": "-1",
                        "left": "-1",
                        "max": "0",
                        "monitor": "-1",
                        "remember": "1",
                        "top": "-1",
                        "width": "-1",
                    }
                },
                "record": {"time": {"first": "0"}},
                "render": {
                    "avalibale": {"directx": "1", "vulkan": "1"},
                    "mode": {
                        "choose": "render.mode.highperformance",
                        "highperformance": "Vulkan",
                    },
                },
                "resolution": {
                    "current": "900.000000:1600.000000:320.000000",
                    "mode": {
                        "choose": "resolution.mode.phone",
                        "custom": "1600.000000:900.000000:240.000000",
                        "intelligence": "1600:900:240",
                        "intelligence_enable": "0",
                        "intelligence_preselect_enable": "0",
                        "phone": "900.000000:1600.000000:320.000000",
                        "tablet": "0.000000:0.000000:0.000000",
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
                        "boss_key": {
                            "conflict": "0",
                            "local_conflict": "0",
                            "text": "Alt+Q",
                        },
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
                        "screenshot": {
                            "conflict": "0",
                            "has_modify": "1",
                            "text": "F9",
                        },
                        "scroll_screen": {"conflict": "0", "text": "null"},
                        "shake": {"conflict": "0", "text": "null"},
                        "start_or_end_operate_record": {
                            "conflict": "0",
                            "text": "null",
                        },
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
                        "zoom_screen": {"conflict": "0", "text": "Ctrl + mouse wheel"},
                    },
                    "mouse_right_btn_as_return_back": "0",
                },
                "toolbar": {"topmost_items": "kUnknown,kKeymap,kVolume,kBack"},
                "ui_setting": {"mode": {"choose": "ui_setting.mode.hideallui"}},
                "video_memory": {
                    "strategy": {"choose": "video_memory.strategy.performance_better"}
                },
                "volume_setting": {
                    "loudspeaker": "Main audio output device",
                    "microphone": "Main audio input device",
                    "system_volume": {"close": "1", "max": "0"},
                },
            },
        }

    try:
        pki = (
            ProcKiller(
                folders=(
                    r"C:\LDPlayer",
                    r"C:\Program Files\Oracle\VirtualBox",
                    r"C:\Program Files\BlueStacks_nxt",
                    r"C:\Program Files\Microvirt",
                    r"C:\Program Files\Netease",
                    r"C:\Program Files\ldplayer9box",
                    r"C:\Program Files\Netease",
                    r"C:\ProgramData\BlueStacks_nxt",
                    r"C:\Program Files\MuMuVMMVbox",
                ),
                kill_timeout=2,
                protect_myself=True,  # important, protect_myselfis False, you might kill the whole python process you are in.
                winkill_sigint_dll=True,  # dll first
                winkill_sigbreak_dll=True,
                winkill_sigint=True,  # exe from outside
                winkill_sigbreak=True,
                powershell_sigint=False,
                powershell_sigbreak=False,
                powershell_close=False,
                multi_children_kill=False,  # try to kill each child one by one
                multi_children_always_ignore_pids=(0, 4),  # ignore system processes
                print_output=True,
                taskkill_as_last_option=True,  # this always works, but it is not gracefully anymore):
                exeendings=(".com", ".exe"),
                filter_function=lambda files: True,
            )
            .get_active_procs()
            .kill_running_procs()
        )

    except Exception as e:
        pass
    sleep(3)

    allinstances = get_folder_file_complete_path(basefolder_vms)

    def convert_value(x):
        try:
            return int(ast.literal_eval(x))
        except Exception:
            return -1

    allinstances = get_folder_file_complete_path(basefolder_vms)
    found_instances_ids = []

    for f in allinstances:
        if f.ext.lower() in [".nemu", ".vdi"]:
            try:
                checked_int_value = convert_value(
                    f.folder.rsplit("-", maxsplit=1)[-1].strip()
                )
                if checked_int_value > -1:
                    found_instances_ids.append([checked_int_value, f])

            except Exception as e:
                pass
    last_instance = int(max([q[0] for q in found_instances_ids]))
    new_instance = last_instance + 1
    alluniquefoldernames_sorted_with_int = sorted(
        found_instances_ids,
        key=lambda co: co[0],
        reverse=True,
    )

    raw_vdi_files = [
        x
        for x in allinstances
        if x.folder.endswith("-base") and x.ext.lower() == ".vdi"
    ]
    base_folder_name = raw_vdi_files[0].folder
    new_folder_name = base_folder_name[:-4] + str(new_instance)
    os.makedirs(new_folder_name, exist_ok=True)
    for wanted_file in raw_vdi_files:
        if wanted_file.file.lower() == "system.vdi":
            new_system_vdi_diff = os.path.join(new_folder_name, "system-diff.vdi")
            shutil.copy(wanted_file.path, new_system_vdi_diff)
            continue
        else:
            file_in_new_folder = os.path.join(new_folder_name, wanted_file.file)
            shutil.copy(wanted_file.path, file_in_new_folder)

    parsed_cfg_data = {}
    for indi, filedata in enumerate(alluniquefoldernames_sorted_with_int):
        if filedata[1].ext.lower() == ".nemu":
            with open(filedata[1].path, "r") as f:
                data = f.read()
            parsed_cfg_data[indi] = {
                "nemu": data,
                "xmldict": xmltodict.parse(data),
                "string": data,
                "strings_with_uuids": [
                    qx for qx in data.splitlines() if regex_for_uuid.search(qx)
                ],
                "filedata_index": filedata[0],
                "filedata": filedata[1],
            }
            dxmlq = xmltodict.parse(data)
            parsed_cfg_data[filedata[1].folder] = dxmlq
    best_hit_key = None
    best_hit_value = -1
    for k, v in parsed_cfg_data.items():
        if v.get("strings_with_uuids"):
            machine_id_int = (
                v["strings_with_uuids"][0]
                .split("}", maxsplit=1)[0]
                .rsplit("-", maxsplit=1)[1]
                .lstrip("0")
            )
            if len(machine_id_int) == 0:
                machine_id_int = 0
            else:
                machine_id_int = int(machine_id_int, base=16)
            if machine_id_int > best_hit_value:
                best_hit_key = k
                best_hit_value = machine_id_int

    def get_new_uuid_from_last_element(value, distance=1):
        out_last_key_value = value.rstrip("}").rsplit("-", maxsplit=1)[1].lstrip("0")
        if len(out_last_key_value) == 0:
            out_last_key_value = 0
        else:
            out_last_key_value = int(out_last_key_value, base=16)
        out_new_key_value = out_last_key_value + distance
        out_new_key_value_in_hex = (
            hex(out_new_key_value).lower().replace("x", "").zfill(12)
        )
        return value.rsplit("-", maxsplit=1)[0] + "-" + out_new_key_value_in_hex + "}"

    uuid_system_original = ""
    uuidtochange = {}
    dxml = parsed_cfg_data[best_hit_key]["xmldict"]
    for value, keys in fla_tu(dxml):
        if keys == ("VirtualBox", "Machine", "@uuid") and str(value).startswith("{"):
            newvalue = get_new_uuid_from_last_element(value, distance=1)
            set_in_original_iter(dxml, keys, newvalue)
        elif keys == ("VirtualBox", "Machine", "@name") or keys == (
            "VirtualBox",
            "Machine",
            "ExtraData",
            "ExtraDataItem",
            1,
            "@value",
        ):
            instancename = new_folder_name.rsplit(os.sep)[-1]
            set_in_original_iter(dxml, keys, instancename)
        elif keys[-1] == "@uuid":
            if value.endswith("-0000-100000000000}"):
                uuid_system_original = value[1:-1]
                continue
            if "-0000-00000" in value:
                new_uuid_value = get_new_uuid_from_last_element(value, distance=1)
                uuidtochange[value.strip("}{")] = {
                    "file": os.path.join(new_folder_name, "system-diff.vdi"),
                    "uuid_new": new_uuid_value,
                }
                set_in_original_iter(dxml, keys, new_uuid_value)
            elif "-0001-0000" in value:
                new_uuid_value = get_new_uuid_from_last_element(value, distance=1)
                uuidtochange[value.strip("}{")] = {
                    "file": os.path.join(new_folder_name, "ota.vdi"),
                    "uuid_new": new_uuid_value,
                }
                set_in_original_iter(dxml, keys, new_uuid_value)
            elif "-0002-0000" in value:
                new_uuid_value = get_new_uuid_from_last_element(value, distance=1)
                uuidtochange[value.strip("}{")] = {
                    "file": os.path.join(new_folder_name, "data.vdi"),
                    "uuid_new": new_uuid_value,
                }
                set_in_original_iter(dxml, keys, new_uuid_value)

    VBOXMANAGE_PATH_SHORT = get_short_path_name_cached(vboxmanage_path)

    vm_config["vm"]["ginstance"] = f"ginstance{1393666633824648104+new_instance}"

    new_vbox_file = os.path.join(
        new_folder_name, new_folder_name.split(os.sep)[-1] + ".nemu"
    )
    with open(new_vbox_file, "w", encoding="utf-8") as f:
        try:
            f.write(xmltodict.unparse(dxml, pretty=True))
        except Exception as e:
            print(e)
    os.makedirs(os.path.join(new_folder_name, "configs"), exist_ok=True)
    path_shell_config = os.path.join(new_folder_name, "configs", "shell_config.json")
    path_vm_config = os.path.join(new_folder_name, "configs", "vm_config.json")
    path_customer_config = os.path.join(
        new_folder_name, "configs", "customer_config.json"
    )

    for file_path, file_content in zip(
        [path_shell_config, path_vm_config, path_customer_config],
        [shell_config, vm_config, customer_config],
    ):
        with open(file_path, "w", encoding="utf-8") as f:
            try:
                f.write(str(file_content))
            except Exception as e:
                pass

    for folder in [
        r"apkWatcher",
        r"configTab",
        r"LocationData",
        r"RunningData",
        r"startup",
        r"ThemeData",
    ]:
        os.makedirs(os.path.join(new_folder_name, "data", folder), exist_ok=True)
        if folder == "configTab":
            with open(
                os.path.join(new_folder_name, "data", folder, "configTab.json"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write("""{"com.mumu.launcher": "keymap"}""")
        if folder == "RunningData":
            with open(
                os.path.join(new_folder_name, "data", folder, "AppRunningData.ini"),
                "w",
                encoding="utf-8",
            ) as f:
                f.write("")
    subprocess.run(
        [VBOXMANAGE_PATH_SHORT, "registervm", new_vbox_file],
        **invisibledict,
    )

    return new_folder_name
