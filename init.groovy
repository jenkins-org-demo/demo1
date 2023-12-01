// JenkinsJobDSL.groovy

job('MyGeneratedJob') {
    scm {
        git('https://github.com/sijonelis/jenkins-template-test.git')
    }
    steps {
        shell('echo "Build steps for the generated job"')
    }
    // Add more configurations as needed
}
