titleBanList = ['.', '/', '?', '"']
contentBanList = ['/', '&#x200B;']

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
            sanitizedInnerText = sanitizedInnerText.replace('AITAH', 'Am I the Dingus')
        return sanitizedInnerText
    
    finalTitle = SanitizeTitle(title)
    finalInnerText = SanitizeInnerText(innerText)

    sanitizedContent = {
        'title': finalTitle,
        'innerText': finalInnerText,
    }

    print(sanitizedContent)
    return sanitizedContent