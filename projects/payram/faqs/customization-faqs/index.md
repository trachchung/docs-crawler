<!-- Source: https://docs.payram.com/faqs/customization-faqs -->

### 
Customization & Access Control
  * [How do I customize the payment page’s branding?](https://docs.payram.com/faqs/customization-faqs#how-do-i-customize-the-payment-pages-branding)
  * [How do I manage user roles and permissions?](https://docs.payram.com/faqs/customization-faqs#how-do-i-manage-user-roles-and-permissions)


#### 
How do I customize the payment page’s branding?
PayRam allows basic branding of the checkout page. In the **project settings** (during setup), you can upload your logo image and set a primary color (hex code) for the theme. These are stored in the project configuration (for example, the JSON `logoPath` and `brandColor` fields). You can also enter custom CSS in the advanced branding section to further tweak styles. In short: specify your logo and colors in the PayRam dashboard (Getting Started → Step 2), and PayRam will use those values on the hosted payment page to match your brand.
#### 
How do I manage user roles and permissions?
When you first set up PayRam, the initial account you create is the **root (admin)** user. From there, in the Dashboard under _Team_ , you can add additional users with designated roles (such as Developer, Finance, Read-Only, etc.) to control access. Each user will have permissions based on their role. Separately, when you generate project API keys, you specify a role name (e.g. `platform_admin`) for that key. In your code, use these API keys (keeping them secret) for backend calls; each key inherits the permissions of its role. In summary, use the Team interface to manage login users and use the project-API-key roles to manage programmatic access.
[PreviousReferral FAQ'schevron-left](https://docs.payram.com/faqs/referral-faqs)[NextDebug FAQ'schevron-right](https://docs.payram.com/faqs/debug-faqs)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
