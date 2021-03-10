public class Version
{
    public static void main(java.lang.String[] args) throws java.lang.Exception
    {
        final var processBuilder = new java.lang.ProcessBuilder("docker", "run", "--rm", "openjdk:slim", "java", "--version");
        java.lang.System.out.println(new java.lang.String(processBuilder.start().getInputStream().readAllBytes(), java.nio.charset.StandardCharsets.UTF_8).split(" ")[1]);
    }
}       
