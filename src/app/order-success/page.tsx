'use client';

import React, { Suspense } from 'react';
import Link from 'next/link';
import { useSearchParams } from 'next/navigation';
import { useLanguage } from '@/context/LanguageContext';
import { CheckCircle2, PackageCheck, Printer, ArrowLeft, ArrowRight, ShieldCheck, Truck } from 'lucide-react';

function OrderSuccessInner() {
  const searchParams = useSearchParams();
  const { dir, t } = useLanguage();

  const orderNumber = searchParams.get('order') || 'MESS-842910';
  const phone = searchParams.get('phone') || '01012345678';

  return (
    <div className="max-w-3xl mx-auto px-4 py-12 space-y-8">
      {/* Celebration Box */}
      <div className="bg-white rounded-3xl border border-slate-200 shadow-card p-8 text-center space-y-4">
        <div className="w-20 h-20 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center mx-auto ring-8 ring-emerald-50/60">
          <CheckCircle2 className="w-10 h-10" />
        </div>

        <h1 className="text-2xl sm:text-3xl font-black text-petrol-950">
          {t('orderSuccessTitle')}
        </h1>

        <p className="text-xs sm:text-sm text-slate-500 max-w-md mx-auto leading-relaxed">
          {t('orderSuccessDesc')}
        </p>

        {/* Order Badge */}
        <div className="p-4 rounded-2xl bg-petrol-50/70 border border-petrol-100 inline-block">
          <span className="text-[11px] text-slate-500 block mb-0.5">{t('orderSuccessSubtitle')}</span>
          <span className="text-xl sm:text-2xl font-black text-petrol-900 font-mono tracking-wider">
            {orderNumber}
          </span>
        </div>

        {/* Action Buttons */}
        <div className="pt-4 flex flex-col sm:flex-row items-center justify-center gap-3">
          <Link
            href={`/track-order?order=${orderNumber}&phone=${phone}`}
            className="w-full sm:w-auto px-6 py-3 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-extrabold text-xs flex items-center justify-center gap-2 shadow-sm"
          >
            <Truck className="w-4 h-4" />
            <span>{t('trackMyOrder')}</span>
            {dir === 'rtl' ? <ArrowLeft className="w-3.5 h-3.5" /> : <ArrowRight className="w-3.5 h-3.5" />}
          </Link>

          <button
            onClick={() => window.print()}
            className="w-full sm:w-auto px-5 py-3 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 font-bold text-xs flex items-center justify-center gap-2"
          >
            <Printer className="w-4 h-4" />
            <span>طباعة ملخص الفاتورة</span>
          </button>
        </div>
      </div>

      {/* Trust & Policy Reminder */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
        <div className="bg-white p-4 rounded-2xl border border-slate-200 flex items-start gap-3">
          <ShieldCheck className="w-5 h-5 text-emerald-600 shrink-0 mt-0.5" />
          <div>
            <h4 className="font-bold text-petrol-900 mb-0.5">الدفع عند الاستلام نقداً (COD)</h4>
            <p className="text-slate-500 text-[11px]">لا تدفع أي مبالغ إلا بعد فحص سلامة كرتونة المنتج وسيريال الوكيل المعتمد.</p>
          </div>
        </div>

        <div className="bg-white p-4 rounded-2xl border border-slate-200 flex items-start gap-3">
          <PackageCheck className="w-5 h-5 text-sky-600 shrink-0 mt-0.5" />
          <div>
            <h4 className="font-bold text-petrol-900 mb-0.5">ضمان واستبدال 14 يوم</h4>
            <p className="text-slate-500 text-[11px]">استبدال فوري للجهاز في حالة وجود أي عيب مصنعي طوال فترة الضمان الرسمية.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function OrderSuccessPage() {
  return (
    <Suspense fallback={<div className="p-12 text-center text-xs text-slate-400">جاري تحميل بيانات الفاتورة...</div>}>
      <OrderSuccessInner />
    </Suspense>
  );
}
