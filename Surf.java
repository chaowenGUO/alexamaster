public class Surf
{
    public static void main(final java.lang.String[] args)
    {
        try (final var playwright = com.microsoft.playwright.Playwright.create())
        {
            final var browser = playwright.chromium().launch(new com.microsoft.playwright.BrowserType.LaunchOptions().setExecutablePath(java.nio.file.Path.of("/usr/bin/google-chrome")).setArgs(java.util.List.of("--disable-gpu")));
            final var context = browser.newContext();
            final var alexamaster = context.newPage();
            alexamaster.navigate("https://www.alexamaster.net/Master/157701");
            final var crunchingbaseteam = browser.newPage();
            crunchingbaseteam.navigate("http://www.crunchingbaseteam.com/view.php?user=chaowenguo", com.microsoft.playwright.Page.NavigateOptions.setTimeout(0));
        }
    }
}
