class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set() 

        for email in emails:
            local, domain = email.split('@')  # split into local part and domain
            if '+' in local:
                local = local[:local.index('+')]  # ignore part after the +
            local = local.replace('.', '')    # removing dot in local
            normalized_email = local + '@' + domain   # combine after altering
            unique_emails.add(normalized_email)  

        return len(unique_emails)  