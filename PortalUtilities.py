import getpass
import portalpy
import csv

def getPortal():
    
    portalUrl           = "" #"https://portalpy.esri.com/arcgis"
    portalAdminName     = raw_input('Username: ') #"portaladmin"
    portalAdminPassword = getpass.getpass() #"portaladmin"

    portal = portalpy.Portal(portalUrl, portalAdminName, portalAdminPassword)
    
    return portal
    
def getGroupMembers():
    
    groupMembers = []
    
    portal = getPortal()
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
    