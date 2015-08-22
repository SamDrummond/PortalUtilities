import getpass
import portalpy
import csv

class Utilities(object):
    
    def __init__(self):
        
        portalUrl           = "https://samdrummonddev.maps.arcgis.com" #"https://portalpy.esri.com/arcgis"
        portalAdminName     = raw_input('Username: ') #"portaladmin"
        portalAdminPassword = getpass.getpass() #"portaladmin"

        self._portal = portalpy.Portal(portalUrl, portalAdminName, portalAdminPassword)
    
    def Group_Members(self):
    
        groupMembers = []
    
        portal = self._portal
        groups = portal.search_groups('a*')
    
        for group in groups:
            id = group['id']
            title = group['title']
        
            groupMembers = portal.get_group_members(id)
        
            for members in groupMembers:
                users['users']
            
                for user in users:
                    groupMembers.append([user, id, title])
                
        resultFile = open("GroupMembership.csv",'wb')
        writer = csv.writer(resultFile, dialect='excel')
        writer.writerow(groupMembers)
    