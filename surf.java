public class Main
{
    public static void main(final java.lang.String[] args)
    {
        try (final var playwright = com.microsoft.playwright.Playwright.create())
        {
            final var browser = playwright.chromium().launch(new com.microsoft.playwright.BrowserType.LaunchOptions().setHeadless(false));
            final var page = browser.newPage();
            page.navigate("http://playwright.dev");
            java.lang.System.out.println(page.title());
        }
    }
}
