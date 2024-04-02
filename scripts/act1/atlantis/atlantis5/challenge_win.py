# Generated by BehavEd
# ( "player wins the kraken challenge" )
setNoCollide("kraken_pillar_atl_b_b", "FALSE" )
setAIActive("kraken", "TRUE" )
heroNoTarget("TRUE" )
enemiesNoTarget("TRUE" )
waittimed ( 1.000 )
trig = getZoneVar("trig" )
trigname = getName(trig )
if trigname == "kraken_trigger01"
     remove ( "hack_clip01", "hack_clip01" )
     cameraMove(" -713.080 3956.500 1577.630 ", 0.000 )
     cameraPan(" 0.000 22.700 151.000 ", 0.000, "FALSE" )
elif trigname == "kraken_trigger02"
     remove ( "hack_clip02", "hack_clip02" )
     cameraMove(" -1316.500 4686.920 1577.630 ", 0.000 )
     cameraPan(" 0.000 22.700 241.000 ", 0.000, "FALSE" )
elif trigname == "kraken_trigger03"
     remove ( "hack_clip03", "hack_clip03" )
     cameraMove(" -2046.920 4083.500 1577.630 ", 0.000 )
     cameraPan(" 0.000 22.700 331.000 ", 0.000, "FALSE" )
else
     remove ( "hack_clip04", "hack_clip04" )
     cameraMove(" -1443.500 3353.080 1577.630 ", 0.000 )
     cameraPan(" 0.000 22.700 61.000 ", 0.000, "FALSE" )
     # ( "add another win" )
endif
wins = getZoneVar("wins" )
wins = iadd(wins, 1 )
setZoneVar("wins", wins )
spawn(trig, "kraken_pillar_fall", "faller", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
killEntity("kraken_pillar_atl_b_b" )
sound (  "PLAY_SOUND", "zone_shared/atlantis/pillar_fall", "", "" )
remove ( trig, trig )
# ( "hurt the kraken here" )
waittimed ( 4.500 )
healthper = fmul(wins, 0.250 )
healthper = fsub(1.000, healthper )
maxhealth = getHealthMax("kraken" )
newhealth = fmul(maxhealth, healthper )
newhealth = fadd(newhealth, 1.000 )
setHealth("kraken", newhealth )
sound (  "PLAY_SOUND", "zone_shared/atlantis/pillar_fall", "", "" )
waittimed ( 3.000 )
# ( "let the next pillar know it's okay to go" )
act("smash_relay", "smash_relay" )
cameraResetOldSchool( )
heroNoTarget("FALSE" )
enemiesNoTarget("FALSE" )
if wins == 4
     spawn("boss_challenge", "Kraken_treasure", "treasure", " 0.000 0.000 0.000 ", " 0.000 0.000 0.000 " )
     setDefaultTarget("" )
     # ( "make the kraken play a different animation if this is the last win" )
     playanim (  "EA_KO_HEAD1", "kraken", "NONE", "alldone" )
     waittimed ( 3.000 )
     act("krakdoor", "krakdoor" )
     setNoCollide("krakdoor", "FALSE" )
     waitsignal ( "alldone" )
     remove ( "kraken", "kraken" )
     awardAchievement("", "defeated_kraken" )
     awardReputation("", 50 )
     setGameFlag("bosses", 8, 1 )
     setEnable("exit_link", "TRUE" )
     setMusicOverride("", 1.000 )
     remove ( "mandoor", "mandoor" )
     sound (  "PLAY_SOUND", "common/game/achievement", "", "" )
     createPopupDialogXml("dialogs/special/kraken_achievement" )
     waittimed ( 0.100 )
     startConversation("act1/atlantis/atlantis5/1_atlantis5_020" )
     setRecallActive("TRUE" )
endif

