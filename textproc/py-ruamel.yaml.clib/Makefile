# $FreeBSD$

PORTNAME=	ruamel.yaml.clib
DISTVERSION=	0.2.0
CATEGORIES=	textproc python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	C based reader/scanner and emitter for ruamel.yaml

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python
USE_PYTHON=	autoplist distutils
POST_PLIST=	fix-plist

post-install:
	${STRIP_CMD} ${STAGEDIR}${PYTHONPREFIX_SITELIBDIR}/_ruamel_yaml.so

fix-plist:
	${REINPLACE_CMD} '/\/ruamel\/yaml\/clib\/__init__\.py$$/d; /\/ruamel\/yaml\/clib\/LICENSE$$/d' ${TMPPLIST}
	${ECHO_CMD} @dir '${PYTHON_SITELIBDIR}/ruamel/yaml/clib' >> ${TMPPLIST}
	${REINPLACE_CMD} -e 's|${PYTHONBASE}/||' -e 's|${LOCALBASE}/||' ${TMPPLIST}

.include <bsd.port.mk>
