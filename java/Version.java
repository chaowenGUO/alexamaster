public class Version
{
    public static void main(final java.lang.String[] args) throws java.lang.Exception
    {
        java.nio.file.Files.writeString(java.nio.file.Path.of(java.lang.System.getenv("GITHUB_ENV")), "JAVA=" + new java.lang.String(new java.lang.ProcessBuilder("docker", "run", "--rm", "openjdk:slim", "java", "--version").start().getInputStream().readAllBytes(), java.nio.charset.StandardCharsets.UTF_8).split(" ")[1]);
    }
}       
