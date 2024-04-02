# Generated by BehavEd
# ( "Loki 2 dies" )
killEntity("destroyer" )
killEntity("lokicrystal" )
waittimed ( 0.100 )
sound (  "PLAY_SOUND", "common/game/achievement", "", "" )
createPopupDialogXml("dialogs/special/loki2_achievement" )
waittimed ( 0.100 )
unlockCharacter("odin", "" )
waittimed ( 0.100 )
unlockCharacter("lokih", "" )
awardAchievement("", "defeated_loki" )
awardReputation("", 125 )
objective ( "Niffleheim_Obj70",  "EOBJCMD_COMPLETE" )
objective ( "Niffleheim_Obj0",  "EOBJCMD_COMPLETE" )
setGameFlag("bosses", 23, 1 )
remove ( "spawntroll", "spawntroll" )
setEnable("sp_doom", "TRUE" )
act("sp_doom", "sp_doom" )
waittimed ( 3.000 )
rand = getZoneVar("hide" )
entname = strcatint("outportal0", rand )
setEnable(entname, "TRUE" )
doorname = strcatint("blockage0", rand )
setEnable(doorname, "TRUE" )
fxname = strcatint("cavefx0", rand )
setEnable(fxname, "TRUE" )
act(doorname, doorname )
act(doorname, doorname )
act(fxname, fxname )
act(fxname, fxname )
overrideFocusToEntity(entname, 2.000 )

