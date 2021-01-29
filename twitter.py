@@ -76,13 +76,13 @@ class Twitter:
                if first_delay is False:
                    first_delay = True
                    continue
                sleep(60)
                sleep(1)
            return ids

        except Exception as ex:
            pass
            print(ex)
            sleep(60)
            sleep(1)
            return list()

    
@ -101,13 +101,13 @@ class Twitter:
                if first_delay is False:
                    first_delay = True
                    continue
                sleep(60)
                
            return ids

        except Exception as ex:
            pass
            print(ex)
            sleep(60)
            
            return list()
    

@ -340,7 +340,7 @@ class Twitter:
                        notif = self.credential.Notify_blacklistWords
                        self.send_dm(recipient_id=sender_id, text=notif)
                    except Exception as ex:
                        sleep(60)
                        
                        print(ex)
                        pass

@ -412,7 +412,7 @@ class Twitter:
        except Exception as ex:
            pass
            print(ex)
            sleep(60)
            
            return dms


@ -446,7 +446,7 @@ class Twitter:
        except Exception as ex:
            pass
            print(ex)
            sleep(60)
            


    def delete_dm(self, id):
@ -457,7 +457,7 @@ class Twitter:
            self.api.destroy_direct_message(id)
        except Exception as ex:
            print(ex)
            sleep(60)
            
            pass
    
    
@ -472,7 +472,7 @@ class Twitter:
        except Exception as ex:
            pass
            print(ex)
            sleep(60)
            


    def get_user_screen_name(self, id):
@ -487,7 +487,7 @@ class Twitter:
        except Exception as ex:
            pass
            print(ex)
            sleep(60)
            
            return "Exception"


@ -601,7 +601,7 @@ class Twitter:
        except Exception as ex:
            pass
            print(ex)
            sleep(60)
            
            return list()


@ -697,7 +697,7 @@ class Twitter:
                        media_ids=list_media_ids[:1][0], possibly_sensitive=possibly_sensitive).id
                
                list_media_ids = list_media_ids[1:] + [[]]
                sleep(30+self.random_time)
                
                # tweet are dynamic here
                tweet = tweet[limit-separator:]
            
@ -718,7 +718,7 @@ class Twitter:

            # When media_ids still exists, It will be attached to the subsequent tweets
            while len(list_media_ids[0]) != 0: # Pay attention to the list format, [[]]
                sleep(30+self.random_time)
                

                print("Posting the rest of media...")
                postid1 = self.api.update_status(
@ -738,5 +738,5 @@ class Twitter:
        except Exception as ex:
            pass
            print(ex)
            sleep(60)
           
            return None
