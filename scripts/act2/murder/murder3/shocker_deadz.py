# Generated by BehavEd
# ( "is this murder3's first playthrough?" )
shock_check = getGameFlag("murder3", 6 )
if shock_check == 0
     # ( "this is the first playthrough--update score and continue" )
     setZoneVar("shock_ded", 1 )
     addSimulatorScore(200000 )
     curr_score = getZoneVar("murder3" )
     if curr_score == 24
          rhino = getZoneVar("rhino_ded" )
          shocker = getZoneVar("shock_ded" )
          if rhino == 1
               if shocker == 1
                    createPopupDialogXml("act2/murder/murder3/million" )
                    setGameFlag("murder3", 6, 1 )
                    setEnable("ball_trigger", "TRUE" )
                    setEnable("ball_triggerCS", "TRUE" )
                    remove ( "pushend1", "pushend1" )
                    remove ( "pushend2", "pushend2" )
                    remove ( "dclip_flippers", "dclip_flippers" )
                    startCutScene("FALSE", "FALSE" )
                    cameraFade(1.000, 1.000 )
                    waittimed ( 1.000 )
                    cameraToLocationAngles(" 1783.860 -1512.530 609.600 ", " 1725.840 -1558.360 542.260 ", 0.000 )
                    cameraFade(0.000, 1.000 )
                    waittimed ( 1.000 )
                    spawnEffect("flipperend1", "base/material/explode/exp_generic_med", " 0.000 0.000 60.000 ", " 0.000 0.000 0.000 " )
                    sound (  "PLAY_SOUND", "zone_shared/fx/little_explosion", "", "" )
                    killEntity("flipperend1" )
                    waittimed ( 0.250 )
                    spawnEffect("flipperend2", "base/material/explode/exp_generic_med", " 0.000 0.000 60.000 ", " 0.000 0.000 0.000 " )
                    sound (  "PLAY_SOUND", "zone_shared/fx/little_explosion", "", "" )
                    killEntity("flipperend2" )
                    waittimed ( 1.000 )
                    cameraFade(1.000, 1.000 )
                    waittimed ( 1.000 )
                    cameraReset( )
                    cameraFade(0.000, 1.000 )
                    waittimed ( 1.000 )
                    startConversation("act2/murder/murder3/2_murder3_060" )
               endif
          endif
     endif
endif
waittimed ( 0.100 )
unlockCharacter("jessica", "" )