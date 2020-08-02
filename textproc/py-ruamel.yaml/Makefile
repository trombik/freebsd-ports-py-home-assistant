# $FreeBSD$

PORTNAME=	ruamel.yaml
DISTVERSION=	0.16.10
CATEGORIES=	textproc python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	YAML 1.2 loader/dumper package for Python

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python
USE_PYTHON=	autoplist distutils

post-install:
	${INSTALL_DATA} ${LICENSE_FILE} ${STAGEDIR}${PYTHON_SITELIBDIR}/ruamel/yaml/LICENSE

.include <bsd.port.mk>
