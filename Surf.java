public class Surf
{
    public static void main(final java.lang.String[] args)
    {
        try (final var playwright = com.microsoft.playwright.Playwright.create())
        {
            final var browser = playwright.chromium().launch(new com.microsoft.playwright.BrowserType.LaunchOptions().setExecutablePath(java.nio.file.Path.of("/usr/bin/google-chrome")).setArgs(java.util.List.of("--disable-gpu")));
            final var page = browser.newPage();
            page.navigate("http://playwright.dev");
            java.lang.System.out.println(page.title());
        }
    }
}
