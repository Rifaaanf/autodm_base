@@ -1,8 +1,8 @@
# Original code by Prieyudha Akadita S.
#     Source: https://https://github.com/ydhnwb/autodm_base

# Re-code by Rif'an Fatoni under MIT License
#     Source: https://github.com/Rifaaanf/autodm_base
# Re-code by Fakhri Catur Rofi under MIT License
#     Source: https://github.com/fakhrirofi/twitter_autobase

from twitter import Twitter
from time import sleep
@ -92,12 +92,11 @@ class Autobase:

                except Exception as ex:
                    print(ex)
                    sleep(60)
                    pass
            
            if 'idle' in indicator:
                indicator.remove('idle')      
            sleep(67)
            


    def __update_dm(self, dms, indicator):
@ -109,7 +108,7 @@ class Autobase:
            indicator.remove('dm_safe')
            dms.extend(dms_new)
            indicator.add('dm_safe')
            sleep(65)
            
    

    def update_local_file(self, sender_id, message, postid):
@ -235,7 +234,7 @@ class Autobase:
                                # credential.Notify_sent is False
                                pass
                            
                            sleep(30+self.tw.random_time)
                            

                        else:
                            # Notify sender, message doesn't meet the algorithm's requirement
@ -243,11 +242,10 @@ class Autobase:

                    except Exception as ex:
                        print(ex)
                        sleep(30)
                        pass

            else:
                sleep(3)
                sleep(1)

            
    def check_file_github(self, new=True):
@ -321,7 +319,7 @@ class Autobase:
                        self.AdminCmd.filename_github = f"{self.bot_username} {datee.year}-{datee.month}-{datee.day}.json"

                else:
                    sleep(60)
                    sleep(1)

            except Exception as ex:
                print(ex)
