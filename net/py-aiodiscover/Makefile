# $FreeBSD$

PORTNAME=	aiodiscover
DISTVERSION=	1.4.2
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Discover hosts on the network via ARP and PTR lookup

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}dnspython>0:dns/py-dnspython@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}ifaddr>0:net/py-ifaddr@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}pyroute2>0:net/py-pyroute2@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
