

class UsersRequest:
  def __init__(self, j_object):
    self.total = j_object['total']
    self.start = j_object['start']
    self.num = j_object['num']
    self.nextStart = j_object['nextStart']
    self.users = []

    for j_object_user in j_object['users']:
        self.users.append(User(j_object_user))


class User:
    def __init__(self, j_object):
        self.username = j_object['username']
        self.id = j_object['id']
        self.fullName = j_object['fullName']
        self.availableCredits = j_object['availableCredits']
        self.assignedCredits = j_object['assignedCredits']
        self.preferredView = j_object['preferredView']
        self.clientApps = j_object['clientApps']
        self.defaultGroupId = j_object['defaultGroupId']
        self.description = j_object['description']
        self.email = j_object['email']
        self.userType = j_object['userType']
        self.idpUsername = j_object['idpUsername']
        self.favGroupId = j_object['favGroupId']
        self.lastLogin = j_object['lastLogin']
        self.mfaEnabled = j_object['mfaEnabled']
        self.validateUserProfile = j_object['validateUserProfile'] if 'validateUserProfile' in j_object else None
        self.privacy = j_object['privacy']
        self.access = j_object['access']
        self.storageUsage = j_object['storageUsage']
        self.storageQuota = j_object['storageQuota']
        self.accountId = j_object['accountId']
        self.role = j_object['role']
        self.level = j_object['level']
        self.userLicenseTypeId = j_object['userLicenseTypeId']
        self.disabled = j_object['disabled']
        self.organization = j_object['organization']
        self.tags = j_object['tags']
        self.culture = j_object['culture']
        self.cultureFormat = j_object['cultureFormat']
        self.region = j_object['region']
        self.units = j_object['units']
        self.thumbnail = j_object['thumbnail']
        self.created = j_object['created']
        self.modified = j_object['modified']
        self.provider = j_object['provider']
        self.groups = j_object['groups']




