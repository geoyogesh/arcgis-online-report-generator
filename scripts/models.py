
class ItemsRequest:
  def __init__(self, j_object):
    self.query = j_object['query']
    self.total = j_object['total']
    self.start = j_object['start']
    self.num = j_object['num']
    self.nextStart = j_object['nextStart']
    self.items = []

    for j_object_group in j_object['results']:
        self.items.append(Item(j_object_group))

class GroupsRequest:
  def __init__(self, j_object):
    self.query = j_object['query']
    self.total = j_object['total']
    self.start = j_object['start']
    self.num = j_object['num']
    self.nextStart = j_object['nextStart']
    self.groups = []

    for j_object_group in j_object['results']:
        self.groups.append(Group(j_object_group))


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


class Group:
    def __init__(self, j_object):
        self.id = j_object['id']
        self.title = j_object['title']
        self.isInvitationOnly = j_object['isInvitationOnly']
        self.owner = j_object['owner']
        self.description = j_object['description']
        self.snippet = j_object['snippet']
        self.tags = j_object['tags']
        self.phone = j_object['phone']
        self.sortField = j_object['sortField']
        self.sortOrder = j_object['sortOrder']
        self.isViewOnly = j_object['isViewOnly']
        self.thumbnail = j_object['thumbnail']
        self.created = j_object['created']
        self.modified = j_object['modified']
        self.access = j_object['access']
        self.capabilities = j_object['capabilities']
        self.isFav = j_object['isFav']
        self.isReadOnly = j_object['isReadOnly']
        self.protected = j_object['protected']
        self.autoJoin = j_object['autoJoin']
        self.notificationsEnabled = j_object['notificationsEnabled']
        self.provider = j_object['provider']
        self.providerGroupName = j_object['providerGroupName']


class Item:
    def __init__(self, j_object):
        self.id = j_object['id']
        self.owner = j_object['owner']
        self.created = j_object['created']
        self.modified = j_object['modified']
        self.guid = j_object['guid']
        self.name = j_object['name']
        self.title = j_object['title']
        self.type = j_object['type']
        self.typeKeywords = j_object['typeKeywords']
        self.description = j_object['description']
        self.tags = j_object['tags']
        self.snippet = j_object['snippet']
        self.thumbnail = j_object['thumbnail']
        self.documentation = j_object['documentation']
        self.extent = j_object['extent']
        self.categories = j_object['categories']
        self.spatialReference = j_object['spatialReference']
        self.accessInformation = j_object['accessInformation']
        self.licenseInfo = j_object['licenseInfo']
        self.culture = j_object['culture']
        self.properties = j_object['properties']
        self.url = j_object['url']
        self.proxyFilter = j_object['proxyFilter']
        self.access = j_object['access']
        self.size = j_object['size']
        self.appCategories = j_object['appCategories']
        self.industries = j_object['industries']
        self.languages = j_object['languages']
        self.largeThumbnail = j_object['largeThumbnail']
        self.banner = j_object['banner']
        self.screenshots = j_object['screenshots']
        self.listed = j_object['listed']
        self.numComments = j_object['numComments']
        self.numRatings = j_object['numRatings']
        self.avgRating = j_object['avgRating']
        self.numViews = j_object['numViews']
        self.scoreCompleteness = j_object['scoreCompleteness']
        self.groupDesignations = j_object['groupDesignations']
