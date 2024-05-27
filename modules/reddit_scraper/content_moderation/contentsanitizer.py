from .ban_lists.titlebanlist import titleBanList as titleBanList
from .ban_lists.contentbanlist import contentBanList as contentBanList

def Sanitize(title, innerText):
    def SanitizeTitle(title):
        sanitizedTitle = title

        for ban in titleBanList:
            sanitizedTitle = sanitizedTitle.replace(ban, '')

        return sanitizedTitle
    
    def SanitizeInnerText(innerText):
        sanitizedInnerText = innerText

        for ban in contentBanList:
            sanitizedInnerText = sanitizedInnerText.replace(ban, '')
            sanitizedInnerText = sanitizedInnerText.replace('AITAH', 'Am I the villian')
        return sanitizedInnerText
    
    finalTitle = SanitizeTitle(title)
    finalInnerText = SanitizeInnerText(innerText)

    sanitizedContent = {
        'title': finalTitle,
        'innerText': finalInnerText,
    }

    print(sanitizedContent)
    return sanitizedContent