'use client';

import React from 'react';
import { useLanguage } from '@/context/LanguageContext';
import { Banknote, Truck, ShieldCheck, RefreshCw } from 'lucide-react';

export default function TrustBar() {
  const { t } = useLanguage();

  const trustItems = [
    {
      icon: <Banknote className="w-7 h-7 text-petrol-700" />,
      title: t('trust_cod_title'),
      desc: t('trust_cod_desc'),
      badge: 'COD',
    },
    {
      icon: <Truck className="w-7 h-7 text-petrol-700" />,
      title: t('trust_shipping_title'),
      desc: t('trust_shipping_desc'),
      badge: '24-48h',
    },
    {
      icon: <ShieldCheck className="w-7 h-7 text-petrol-700" />,
      title: t('trust_authentic_title'),
      desc: t('trust_authentic_desc'),
      badge: '100%',
    },
    {
      icon: <RefreshCw className="w-7 h-7 text-petrol-700" />,
      title: t('trust_warranty_title'),
      desc: t('trust_warranty_desc'),
      badge: '14 Days',
    },
  ];

  return (
    <section className="bg-white border-y border-slate-200/80 py-5 shadow-subtle">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {trustItems.map((item, index) => (
            <div
              key={index}
              className="flex items-start gap-3.5 p-3 rounded-xl hover:bg-petrol-50/50 transition-colors group"
            >
              <div className="w-12 h-12 rounded-xl bg-petrol-100 flex items-center justify-center shrink-0 group-hover:scale-105 group-hover:bg-petrol-200 transition-all">
                {item.icon}
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <h4 className="font-bold text-sm text-petrol-900 leading-snug">{item.title}</h4>
                  <span className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-petrol-50 text-petrol-700 border border-petrol-200">
                    {item.badge}
                  </span>
                </div>
                <p className="text-xs text-slate-500 leading-relaxed">{item.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
