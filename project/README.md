# Security Analysis Utility (SAU)

## New Plan

Replicate the GitHub security feature using RMarkdown. Possibly 
extend the feature using a decision tree.

## Old Plan

After wandering around in the desert for 40 days,
it turns out that the Spring Framework doesn't currently
support an OAuth2 Authorization Server.

* [29.3.3 Authorization Server](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#_authorization_server)

It links you to 

* [6.8 OAuth 2.0 Resource Server](https://docs.spring.io/spring-security/site/docs/current/reference/htmlsingle/#oauth2client)
* [OAuth2 Boot](https://docs.spring.io/spring-security-oauth2-boot/docs/2.2.x-SNAPSHOT/reference/html5/)

These projects are either deprecated or do not contain an
authorization server whatsoever. Previous implementations 
of the Authorization Server no longer build successfully. 

The lack of support for an authorization server means I'll have
to really think about a Plan B.



If I can't replicate the GitHub feature by midterm time then I'll
have to ditch this approach and write a research paper.


## References

* [Spring Security and Angular](https://spring.io/guides/tutorials/spring-security-and-angular-js/)
* [Our Software Dependency Problem](https://research.swtch.com/deps)
* [spring-guides/tut-spring-security-and-angular-js](https://github.com/spring-guides/tut-spring-security-and-angular-js)
